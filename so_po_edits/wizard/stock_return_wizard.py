from odoo import _, api, fields, models, SUPERUSER_ID


class StockReturnWizard(models.TransientModel):
    _name = "stock.return.wizard"
    _description = "Stock Return Wizard"

    move_id = fields.Many2one(
        'account.move',
        readonly=True
    )
    move_type = fields.Selection(
        related='move_id.move_type'
    )
    vendor_location_id = fields.Many2one(
        'stock.location',
        string="Destination Location",
        domain="[('usage', '=', 'supplier')]"
    )
    location_id = fields.Many2one(
        'stock.location',
    )
    customer_location_id = fields.Many2one(
        'stock.location',
        domain="[('usage', '=', 'customer')]"
    )
    line_ids = fields.One2many(
        'stock.return.line',
        'stock_return_id',
        compute='compute_line_ids',
        store=1,
        readonly=False
    )

    @api.depends('move_id')
    def compute_line_ids(self):
        if self.move_id:
            if self.move_type == 'in_refund':
                vendor_location = self.env['stock.location'].sudo().search([
                    ('usage', '=', 'supplier')
                ], limit=1)
                if vendor_location:
                    self.vendor_location_id = vendor_location
            if self.move_type == 'out_refund':
                customer_location = self.env['stock.location'].sudo().search([
                    ('usage', '=', 'customer')
                ], limit=1)
                if customer_location:
                    self.customer_location_id = customer_location
            lines = self.move_id.invoice_line_ids.filtered(
                lambda line: line.product_id.detailed_type in ['consu', 'product'])
            for line in lines:
                record = self.env['stock.return.line'].with_user(SUPERUSER_ID).create({
                    'stock_return_id': self._origin.id,
                    'product_id': line.product_id.id,
                    'quantity': line.quantity
                })
                self.line_ids = [(4, record.id)]
        else:
            self.line_ids = []

    def action_stock_return(self):
        picking_type = None
        if self.move_type == 'in_refund':
            picking_type = self.location_id.warehouse_id.out_type_id
        elif self.move_type == 'out_refund':
            picking_type = self.location_id.warehouse_id.in_type_id
        picking_vals = {
            'partner_id': self.move_id.partner_id.id,
            'picking_type_id': picking_type.id if picking_type else False,
            'location_id': self.location_id.id if self.move_type == 'in_refund' else self.customer_location_id.id,
            'location_dest_id': self.vendor_location_id.id if self.move_type == 'in_refund' else self.location_id.id,
            'origin': self.move_id.name,
            "move_ids_without_package": [
                (0, 0, {
                    'product_id': rec.product_id.id,
                    'product_uom_qty': rec.quantity,
                    'quantity': rec.quantity,
                    'location_id': self.location_id.id if self.move_type == 'in_refund' else self.customer_location_id.id,
                    'location_dest_id': self.vendor_location_id.id if self.move_type == 'in_refund' else self.location_id.id,
                    'name': rec.product_id.name,
                })
                for rec in self.line_ids
            ],
        }
        picking = self.env['stock.picking'].sudo().create(picking_vals)
        if picking:
            self.move_id.return_picking_id = picking.id
        return {
            'name': 'Stock Picking',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'stock.picking',
            'res_id': picking.id if picking else False,
            'target': 'current'
        }


class StockReturnLine(models.TransientModel):
    _name = "stock.return.line"
    _description = "Stock Return Line"

    stock_return_id = fields.Many2one(
        'stock.return.wizard'
    )
    product_id = fields.Many2one(
        'product.product',
        domain="[('id', '=', product_id)]",
        required=True,
    )
    quantity = fields.Float()
