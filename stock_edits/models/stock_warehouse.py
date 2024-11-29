from odoo import _, api, fields, models


class StockWarehouse(models.Model):
    _inherit = "stock.warehouse"
    _description = "Stock Warehouse Inherit"

    sales_journal_id = fields.Many2one(
        'account.journal',
        domain="[('type', '=', 'sale')]"
    )

