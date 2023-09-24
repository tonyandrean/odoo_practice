from dataclasses import field
from datetime import timedelta, datetime
from odoo import models, fields, api
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning


class PinjamBuku (models.Model):
    _name = 'pinjam.buku'
    _inherit = ['mail.thread']
    _description = 'Peminjaman Buku Perpustakaan'
    _rec_name = 'pj_id_number'

    pj_judul_id = fields.Many2one('daftar.buku', string='Judul Buku', required=True)
    pj_penulis_id = fields.Many2many('master.penulis', string='Penulis', compute='_compute_penulis')
    pj_peminjam_id = fields.Many2one('res.users', string='Peminjam', default=lambda self: self.env.user)
    pj_id_number = fields.Char(string='ID Number')
    pj_tgl_pinjam = fields.Datetime(string='Tanggal Pinjam', default=fields.Datetime.now)
    pj_tgl_balik = fields.Datetime(string='Tanggal Pengembalian')
    pj_maks_balik = fields.Datetime(string='Maksimal Pengembalian', default=lambda
                                    self: fields.Datetime.now() + timedelta(minutes=1))
    status_bar = fields.Selection(selection=[('draft', 'Draft'), ('in_progress', 'In Progress'),
                                             ('return', 'Return'), ('overdue', 'Overdue')],
                                             string='Status', required=True, copy=False, tracking=True, default='draft')

# otomatis isi field penulis
    @api.depends('pj_judul_id')
    def _compute_penulis(self):
        for record in self:
            if record.pj_judul_id:
                record.pj_penulis_id = record.pj_judul_id.bk_penulis_id
            else:
                record.pj_penulis_id = False

#membuat id peminjaman
    @api.model
    def create(self, vals):
        vals['pj_id_number'] = self.env['ir.sequence'].next_by_code('pinjam.buku')
        return super(PinjamBuku, self).create(vals)

# mengatur status bar dengan button
    def button_in_progress(self):
        if self.pj_judul_id.bk_stock <= 0:
            raise UserError(
                'Maaf stok buku sedang habis, silahkan coba lain waktu.')
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
        if self.pj_maks_balik < fields.Datetime.now():
            self.write({'status_bar': 'overdue'})
        else:
            self.write({'status_bar': 'return'})
        self.write({'pj_tgl_balik': fields.Datetime.now()})
        self.pj_judul_id.write({'bk_stock': self.pj_judul_id.bk_stock + 1})
        return {
            'type': 'ir.actions.act_window',
            'name': 'Peminjaman Buku Perpustakaan',
            'res_model': 'pinjam.buku',
            'view_mode': 'tree,form',
            'target': 'main',
        }

# mengembalikan stok buku ketika record dihapus
    def unlink(self):
        for record in self:
            if record.status_bar == 'in_progress':
                record.pj_judul_id.write({'bk_stock': record.pj_judul_id.bk_stock + 1})
        return super(PinjamBuku, self).unlink()