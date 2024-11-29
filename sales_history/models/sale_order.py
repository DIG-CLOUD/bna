# -*- coding: utf-8 -*-
from odoo import models,fields,api,_
from odoo.exceptions import UserError,ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.onchange('order_line')
    def _check_product_existing(self):
        if self.order_line:
            for order in self:
                products_in_lines = order.mapped('order_line.product_id')
                for product in products_in_lines:
                    lines_count = len(order.order_line.filtered(lambda line: line.product_id == product))
                    if lines_count > 1:
                        raise ValidationError(_('This Product already Added To the List'))
   