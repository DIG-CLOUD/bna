from odoo import _, api, fields, models


class EmployeeBranch(models.Model):
    _name = "employee.branch"
    _description = "Employee Branch"

    name = fields.Char()
