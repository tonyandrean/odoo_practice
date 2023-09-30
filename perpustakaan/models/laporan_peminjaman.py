from odoo import models, fields, api
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning


class LaporanPeminjaman(models.Model):
    _name = 'laporan.pinjam'
    _inherit = ['mail.thread']
    _description = 'Laporan Peminjaman Buku Perpustakaan'
    _rec_name = 'lp_id_number'

    lp_id_number = fields.Many2one('pinjam.buku', string='ID Peminjaman', required=True)
    lp_judul_id = fields.Many2one(string='Judul Buku', related='lp_id_number.pj_judul_id', store=True)
    lp_penulis_id = fields.Many2many(string='Penulis', related='lp_id_number.pj_judul_id.bk_penulis_id')
    lp_kategori_id = fields.Many2one(string='Kategori', related='lp_id_number.pj_judul_id.bk_kategori_id', store=True)
    lp_peminjam_id = fields.Many2one(string='Peminjam', related='lp_id_number.pj_peminjam_id', store=True)
    lp_status_bar = fields.Selection(selection=[('draft', 'Draft'), ('in_progress', 'In Progress'),
                                                ('return', 'Return'), ('overdue', 'Overdue')],
                                                string='Status', related='lp_id_number.status_bar')