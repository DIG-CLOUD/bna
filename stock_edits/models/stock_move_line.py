from odoo import _, api, fields, models


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"
    _description = "Stock Move Line Inherit"

    picking_partner_id = fields.Many2one(
        store=1
    )
    so = fields.Many2one(
        related="move_id.sale_line_id",
    )
    po = fields.Many2one(
        related="move_id.purchase_line_id",
    )
    price_unit = fields.Float(
        compute="compute_price_unit"
    )

    def compute_price_unit(self):
        for rec in self:
            if rec.po:
                rec.price_unit = rec.move_id.purchase_line_id.price_unit
            elif rec.so:
                rec.price_unit = rec.move_id.sale_line_id.price_unit
            else:
                rec.price_unit = 0
