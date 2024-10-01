from odoo import models, fields



class ResBranch(models.Model):
    _name = 'res.branch'
    _description = 'Branch for user'



    name = fields.Char(string='Branch')
    code = fields.Char(string='Code')