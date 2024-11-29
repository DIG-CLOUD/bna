from odoo import _, api, fields, models


class AccountMove(models.Model):
    _inherit = "account.move"
    _description = "Account Move Inherit"

    total_quantity = fields.Float(
        compute='_compute_total_quantity'
    )
    return_picking_id = fields.Many2one(
        'stock.picking',
        readonly=1
    )
    is_indexed = fields.Boolean()

    @api.depends('invoice_line_ids')
    def _compute_total_quantity(self):
        for rec in self:
            rec.total_quantity = sum(rec.invoice_line_ids.mapped('quantity'))

    @api.constrains('invoice_line_ids')
    @api.onchange('invoice_line_ids')
    def _check_invoice_line_ids(self):
        for idx, line in enumerate(self.invoice_line_ids):
            line.index = idx + 1

    def stock_return(self):
        return {
            'name': _('Stock Return'),
            'type': 'ir.actions.act_window',
            'res_model': 'stock.return.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_move_id': self.id,
            }
        }

    def add_index_action(self):
        for rec in self:
            if not rec.is_indexed:
                for idx, line in enumerate(rec.invoice_line_ids):
                    line.index = idx + 1
            rec.is_indexed = True
