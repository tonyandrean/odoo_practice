from dataclasses import field
from odoo import models, fields, api
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning

class DaftarBuku (models.Model):
    _name = 'daftar.buku'
    _inherit = ['mail.thread']
    _description = 'Daftar Buku Perpustakaan'
    _rec_name='bk_judul'

    bk_judul = fields.Char(string='Judul Buku', required=True)
    bk_penulis_id = fields.Many2many('master.penulis', string='Penulis', required=True)
    bk_th_terbit = fields.Char(string='Tahun Terbit', size=4, required=True)
    bk_penerbit_id = fields.Many2one('master.penerbit', string='Penerbit', required=True)
    bk_halaman = fields.Integer(string='Jumlah Halaman')
    bk_isbn = fields.Char(string='ISBN', size=13, required=True)
    bk_kategori_id = fields.Many2one('master.kategori', string='Kategori Buku', required=True)
    bk_stock = fields.Integer(string='Stok', required=True)