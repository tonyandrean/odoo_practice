from dataclasses import field
from odoo import models, fields, api
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning

class AkunAnggota(models.Model):
    _name = 'info.anggota'
    _inherit = ['mail.thread']
    _description = 'Akun Anggota Perpustakaan'
    _rec_name='an_username'

    an_username = fields.Char(string='Username', required=True)
    an_name = fields.Char(string='Nama', required=True)
    an_alamat = fields.Text(string='Alamat')
    an_email = fields.Char(string='E-mail', required=True)
    
    an_user_id = fields.Many2one(comodel_name='info.anggota', string='user_ID', track_visibility='onchange')
    an_id_user = fields.Many2one(comodel_name='res.users', string='User ID')
    an_id_number = fields.Char(string='ID Number', track_visibility='onchange')

    # create  user_id  and id number using sequence_id
    @api.model
    def create(self, vals):
        vals['an_id_number'] = self.env['ir.sequence'].next_by_code(
            'info.anggota')
        new_user = {
            'password': 'Perpus123',
            'login': vals['an_username'],
            'name': vals['an_name'],
            'email': vals['an_email']
        }
        user = self.env['res.users'].search([('login', '=', vals['an_username'])])
        if user:
            raise UserError(("Anggota dengan Username ini sudah ada"))
        else:
            new_user = self.env['res.users'].create(new_user)
            vals.update({'an_id_user': new_user.id})
        res = super(AkunAnggota, self).create(vals)
        return res
    
class AkunAdmin (models.Model):
    _name = 'info.admin'
    _inherit = ['mail.thread']
    _description = 'Akun Admin Perpustakaan'
    _rec_name='ad_username'

    ad_username = fields.Char(string='Username', required=True)
    ad_name = fields.Char(string='Nama', required=True)
    ad_alamat = fields.Text(string='Alamat')
    ad_email = fields.Char(string='E-mail', required=True)
    
    ad_user_id = fields.Many2one(comodel_name='info.admin', string='user_ID', track_visibility='onchange')
    ad_id_user = fields.Many2one(comodel_name='res.users', string='User ID')
    ad_id_number = fields.Char(string='ID Number', track_visibility='onchange')

    # create  user_id  and id number using sequence_id
    @api.model
    def create(self, vals):
        vals['ad_id_number'] = self.env['ir.sequence'].next_by_code(
            'info.admin')
        new_user = {
            'password': 'Admin123',
            'login': vals['ad_username'],
            'name': vals['ad_name'],
            'email': vals['ad_email']
        }
        user = self.env['res.users'].search([('login', '=', vals['ad_username'])])
        if user:
            raise UserError(("Admin dengan Username ini sudah ada"))
        else:
            new_user = self.env['res.users'].create(new_user)
            vals.update({'ad_id_user': new_user.id})
        res = super(AkunAdmin, self).create(vals)
        return res