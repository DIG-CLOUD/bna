from odoo import _, api, fields, models


class HrEmployeeInherit(models.Model):
    _inherit = "hr.employee"
    _description = "Hr Employee Inherit"

    employee_code = fields.Char()
    joining_date = fields.Date()
    branch_id = fields.Many2one('employee.branch')
    degree = fields.Char()
    religion = fields.Char()
    id_hijri_expire_date = fields.Char()
    passport_end_date = fields.Date()
    iqama_job_title = fields.Char()
    iqama_release_date = fields.Date()
    iqama_end_date = fields.Date()
    employer_phone = fields.Char()
    outside_kingdom = fields.Char()
