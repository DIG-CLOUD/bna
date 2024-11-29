# -*- coding: utf-8 -*-
from odoo import models,fields,api,_
from odoo.exceptions import UserError 

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    validity_date = fields.Date("Confirmation Date",related='order_id.validity_date',readonly=True,store=True)
    @api.onchange('product_id')
    def _onchange_product_id(self):
        if self.product_id:
            so = self.env['sale.order'].search([
                ('partner_id','=',self.order_id.partner_id.id),
                ('order_line.product_id','=',self.product_id.id),
                ('state', 'in', ('sale', 'done'))], order="id desc", limit=1)
            if so:
                self.price_unit=so.order_line[0].price_unit
    
    def action_sale_history(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("sales_history.action_sale_history")
        action['domain'] = [('state', 'in', ['sale', 'done']), ('product_id', '=', self.product_id.id)]
        action['display_name'] = _("Sales History for %s", self.product_id.display_name)
        action['context'] = {
            'search_default_order_partner_id': self.order_partner_id.id
        }
        return action
