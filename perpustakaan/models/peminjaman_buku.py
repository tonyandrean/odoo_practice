from dataclasses import field
from datetime import timedelta, datetime
from odoo import models, fields, api
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning

class PinjamBuku (models.Model):
    _name = 'pinjam.buku'
    _inherit = ['mail.thread']
    _description = 'Peminjaman Buku Perpustakaan'
    _rec_name='pj_judul_id'

    pj_judul_id = fields.Many2one('daftar.buku', string='Judul Buku', required=True)
    pj_penulis_id = fields.Many2many('master.penulis', string='Penulis', compute='_compute_penulis')
    pj_tgl_pinjam = fields.Datetime(string='Tanggal Pinjam', default=fields.Datetime.now)
    pj_tgl_balik = fields.Datetime(string='Tanggal Kembali', default=lambda self: fields.Datetime.now() + timedelta(days=7))

    #otomatis isi field penulis
    @api.depends('pj_judul_id')
    def _compute_penulis(self):
        for record in self:
            if record.pj_judul_id:
                record.pj_penulis_id = record.pj_judul_id.bk_penulis_id
            else:
                record.pj_penulis_id = False