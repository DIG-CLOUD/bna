from odoo import _, api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"
    _description = "Sale Order Inherit"

    total_quantity = fields.Float(
        compute='_compute_total_quantity'
    )

    @api.depends('order_line')
    def _compute_total_quantity(self):
        for rec in self:
            rec.total_quantity = sum(rec.order_line.mapped('product_uom_qty'))
