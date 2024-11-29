from odoo import _, api, fields, models


class HrContractInherit(models.Model):
    _inherit = "hr.contract"
    _description = "Hr Contract Inherit"

    type_of_contract = fields.Char()
    period = fields.Selection([
        ('year', 'Year'),
        ('1.5year', '1.5 Year'),
        ('2years', '2 Years'),
        ('custom', 'Custom'),
    ])
    days_before = fields.Integer()
