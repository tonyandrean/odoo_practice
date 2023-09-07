#import the libraries
from dataclasses import field
from odoo import models, fields,api
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning

class master_dosen(models.Model):
    _name='dosen.dosen'
    _inherit = ['mail.thread']
    _description='Data Dosen'
    _rec_name='name'
    _sql_constraints = [
        ('name', 'unique(name)', 'Nama Dosen already exist !')
    ]

    name=fields.Char(string='Nama Dosen')
    prodi= fields.Char(string='Program Studi')
    description=fields.Text(string='Deskripsi')