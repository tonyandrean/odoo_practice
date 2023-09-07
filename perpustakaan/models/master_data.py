from dataclasses import field
from odoo import models, fields, api
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning


class MasterPenulis (models.Model):
    _name = 'master.penulis'
    _inherit = ['mail.thread']
    _description = 'Master Data Penulis'
    _rec_name='m_penulis'
    _sql_constraints = [
        ('m_penulis_uniq', 'unique(m_penulis)', 'Nama Penulis already exist !')
    ]

    m_penulis = fields.Char(string='Penulis', required=True)
    description = fields.Text(string='Deskripsi')

class MasterPenerbit (models.Model):
    _name = 'master.penerbit'
    _inherit = ['mail.thread']
    _description = 'Master Data Penerbit'
    _rec_name='m_penerbit'
    _sql_constraints = [
        ('m_penerbit_uniq', 'unique(m_penerbit)', 'Nama Penerbit already exist !')
    ]
    
    m_penerbit = fields.Char(string='Penerbit', required=True)
    description = fields.Text(string='Deskripsi')

class MasterKategori (models.Model):
    _name = 'master.kategori'
    _inherit = ['mail.thread']
    _description = 'Master Data Kategori'
    _rec_name='m_kategori'
    _sql_constraints = [
        ('m_kategori_uniq', 'unique(m_kategori)', 'Nama Kategori already exist !')
    ]

    m_kategori = fields.Char(string='Kategori')
    description = fields.Text(string='Deskripsi')