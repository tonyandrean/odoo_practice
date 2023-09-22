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
    pj_peminjam_id = fields.Many2one('res.users', string='Peminjam', default=lambda self: self.env.user)
    pj_tgl_pinjam = fields.Datetime(string='Tanggal Pinjam', default=fields.Datetime.now)
    pj_tgl_balik = fields.Datetime(string='Tanggal Kembali', default=lambda 
                                   self: fields.Datetime.now() + timedelta(hours=1))
    status_bar = fields.Selection(selection=[('draft', 'Draft'), ('in_progress', 'In Progress'), 
                                             ('return', 'Return')], string='Status', required=True, 
                                             copy=False, tracking=True, default='draft')

    #otomatis isi field penulis
    @api.depends('pj_judul_id')
    def _compute_penulis(self):
        for record in self:
            if record.pj_judul_id:
                record.pj_penulis_id = record.pj_judul_id.bk_penulis_id
            else:
                record.pj_penulis_id = False

    #mengatur status bar dengan button
    def button_in_progress(self):
        if self.pj_judul_id.bk_stock <= 0:
            raise UserError('Maaf stok buku sedang habis, silahkan coba lain waktu.')
        else:
            self.pj_judul_id.write({'bk_stock': self.pj_judul_id.bk_stock - 1})
            self.write({'status_bar': 'in_progress'})
            return {
                'type': 'ir.actions.act_window',
                'name': 'Peminjaman Buku Perpustakaan',
                'res_model': 'pinjam.buku',
                'view_mode': 'tree,form',
                'target': 'main',
            }
    
    def button_return(self):
        self.pj_judul_id.write({'bk_stock': self.pj_judul_id.bk_stock + 1})
        self.write({'status_bar': 'return'})
        return {
            'type': 'ir.actions.act_window',
            'name': 'Peminjaman Buku Perpustakaan',
            'res_model': 'pinjam.buku',
            'view_mode': 'tree,form',
            'target': 'main',
        }

    #mengubah status bar ke return jika tanggal kembali terlewat
    @api.onchange('pj_tgl_balik')
    def _onchange_pj_tgl_balik(self):
        for record in self:
            if record.status_bar == 'in_progress' and record.pj_tgl_balik < fields.Datetime.now():
                record.status_bar = 'return'
                record.pj_judul_id.write({'bk_stock': record.pj_judul_id.bk_stock + 1})

    #mengembalikan stok buku ketika record dihapus
    def unlink(self):
        for record in self:
            if record.pj_judul_id:
                record.pj_judul_id.write({'bk_stock': record.pj_judul_id.bk_stock + 1})
        return super(PinjamBuku, self).unlink()