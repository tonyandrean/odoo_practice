#import the libraries
from dataclasses import field
from odoo import models, fields, api, _
from odoo.exceptions import Warning ,ValidationError

#define class of models survey
class jurnal_reputasi(models.Model):
    _name = 'jurnal.reputasi'
    _inherit = ['mail.thread']
    _rec_name='isbn'
    _description = 'Jurnal Internasional Bereputasi'

    #penulis = fields.Char(string='Penulis')
    penulis_id = fields.Many2many('dosen.dosen', string='Penulis')
    jurusan_id=fields.Many2one('jurusan.jurusan', string='Program Studi')
    judul = fields.Char(string='Judul Artikel')
    nama_jurnal = fields.Char(string='Nama Jurnal')
    publisher = fields.Char(string='Publisher')
    indek_id = fields.Many2many('index.index', string='Indeks')
    #indeks = fields.Char(string='Indeks')
    kuartil = fields.Selection(string='Kuartil (Q)', selection=[('q1', 'Q1'), ('q2', 'Q2'), ('q3', 'Q3'), ('q4', 'Q4')])
    isbn = fields.Char(string='ISBN/ISSN')
    tahun = fields.Char(string='Tahun', size=4)
    volume = fields.Integer(string='Volume')
    nomor = fields.Integer(string='No.')
    url = fields.Char(string='URL')
    documents = fields.Binary(string='Dokumen Pendukung')
    file_name=fields.Char(string='File Name')

    @api.onchange('indek_id')
    def onchangeindek_id(self):
        if not self.indek_id:
            self.kuartil = False
        else:
            if len(self.indek_id.ids) == 1:
                for zz in self.indek_id:
                    if zz.name == '':
                        self.kuartil = False

    @api.depends('indek_id')
    def dependindex(self):
        for line in self:
            cekindex = True
            if not line.indek_id:
                cekindex = False
            else:
                if len(line.indek_id.ids) == 1:
                    for zz in line.indek_id:
                        if zz.name == '':
                            cekindex = False
            line.index_kosong = cekindex

    index_kosong = fields.Boolean(default=False, compute='dependindex')

    #indek = tidak terindex, kuartil false
    # @api.onchange('indek_id')
    # def onchangeindek_id(self):
    #     if not self.indek_id:
    #         self.kuartil = False
    #     else:
    #         if len(self.indek_id.ids) == 1:
    #             for zz in self.indek_id:
    #                 if zz.name == 'tidak terindex':
    #                     self.kuartil = False

    # @api.depends('indek_id')
    # def dependindex(self):
    #     for line in self:
    #         cekindex = True
    #         if not line.indek_id:
    #             cekindex = False
    #         else:
    #             if len(line.indek_id.ids) == 1:
    #                 for zz in line.indek_id:
    #                     if zz.name == 'tidak terindex':
    #                         cekindex = False
    #         line.index_kosong = cekindex