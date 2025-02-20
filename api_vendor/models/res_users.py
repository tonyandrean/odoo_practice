from odoo import models, fields, api
import secrets


class ResUsers(models.Model):
    _inherit = 'res.users'


    api_key = fields.Char(string='Api Key', copy=False)

    def generate_api_key(self):
        self.ensure_one()
        self.api_key = secrets.token_hex(32)
        return self.api_key
