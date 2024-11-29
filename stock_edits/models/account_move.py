from odoo import _, api, fields, models


class AccountMove(models.Model):
    _inherit = "account.move"
    _description = "Account Move Inherit"

    def change_invoice_journal(self):
        for rec in self:
            if rec.move_type == 'out_invoice':
                source_orders = self.line_ids.sale_line_ids.order_id
                if source_orders and source_orders[0].warehouse_id:
                    if source_orders[0].warehouse_id.sales_journal_id:
                        rec.journal_id = source_orders[0].warehouse_id.sales_journal_id

