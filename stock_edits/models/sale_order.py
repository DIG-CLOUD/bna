from odoo import _, api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"
    _description = "Sale Order Inherit"

    def _prepare_invoice(self):
        res = super(SaleOrder, self)._prepare_invoice()
        if self.warehouse_id.sales_journal_id:
            res.update({
                'journal_id': self.warehouse_id.sales_journal_id.id,
            })
        return res
