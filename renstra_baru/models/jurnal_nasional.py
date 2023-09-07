# import the libraries
from dataclasses import field
from odoo import models, fields, api

# define class of models survey

class jurnal_nasional(models.Model):
    _name = 'jurnal.nasional'
    _inherit = ['mail.thread']
    _description = 'Jurnal Nasional Terakreditasi'
    _rec_name = 'isbn'

    judul = fields.Char(string='Judul Artikel')
    penulis_id = fields.Many2many('dosen.dosen', string='Penulis')
    fakultas_id=fields.Many2one('fakultas.fakultas', string='Fakultas')
    jurusan_id=fields.Many2one('jurusan.jurusan', string='Program Studi')
    
    # Ini adalah field untuk menyimpan data jurnal
    nama_jurnal = fields.Char(string='Nama Jurnal')
    peringkat_sinta= fields.Selection(string = 'Sinta', selection =[('s1', 'Sinta 1'), ('s2', 'Sinta 2'), ('s3', 'Sinta 3'), ('s4', 'Sinta 4'), ('s5', 'Sinta 5'), ('s6', 'Sinta 6')], required=False)
    isbn = fields.Char(string = 'ISBN/ISSN')
    tahun = fields.Char(string='Tahun', size=4)
    volume = fields.Integer(string='Volume')
    nomor = fields.Integer(string='No.')
    url = fields.Char(string='URL')
    documents = fields.Binary(string='Dokumen Pendukung')
    file_name=fields.Char(string='File Name')