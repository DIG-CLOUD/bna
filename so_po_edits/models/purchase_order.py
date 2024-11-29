from odoo import _, api, fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"
    _description = "Purchase Order Inherit"

    total_quantity = fields.Float(
        compute='_compute_total_quantity'
    )

    @api.depends('order_line')
    def _compute_total_quantity(self):
        for rec in self:
            rec.total_quantity = sum(rec.order_line.mapped('product_qty'))

    def _get_name_po_report(self):
        self.ensure_one()
        return 'po_customize'
