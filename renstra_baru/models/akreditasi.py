#import the libraries
from dataclasses import field
from odoo import models, fields,api
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning


class master_fakultas(models.Model):
    _name='fakultas.fakultas'
    _inherit = ['mail.thread']
    _description='Data Fakultas'
    _rec_name='name'
    _sql_constraints = [
        ('name', 'unique(name)', 'Nama Fakultas already exist !')
    ]

    name=fields.Char(string='Nama Fakultas')
    description=fields.Text(string='Deskripsi')

class master_jurusan(models.Model):
    _name='jurusan.jurusan'
    _inherit = ['mail.thread']
    _description='Data Jurusan'
    _rec_name='name'
    _sql_constraints = [
        ('kode', 'unique(kode)', 'Kode Jurusan already exist !'),
        ('name', 'unique(name)', 'Nama Jurusan already exist !')
    ]

    kode=fields.Char(string='Kode Jurusan')
    name=fields.Char(string='Nama Jurusan')
    fakultas_id=fields.Many2one('fakultas.fakultas', string='Fakultas')
    description=fields.Text(string='Deskripsi')

#define the class of akreditasi database
class akreditasi_banpt(models.Model):
    #define the models name and the description
    _name='akreditasi.ban.pt'
    _inherit = ['mail.thread']
    _description='Input data for acreditaion BAN PT'

    #define periode fields
    periode = fields.Char(string='Periode')

    #define the kode jurusan fields
    kode = fields.Char(string='Kode', related='jurusan_id.kode')
    jurusan_id=fields.Many2one('jurusan.jurusan', string='Program Studi')

    #define the faculty fields from 
    fakultas_id=fields.Many2one('fakultas.fakultas', string='Fakultas')

    #define nomor sk fields
    nomor_sk = fields.Char(string='Nomor SK')

    #define tanggal SK fields
    tanggal = fields.Date(string='Tanggal SK')

    #define the akreditation selection
    select_akreditation=([('a','A'),('unggul','Unggul'),('b','B'),('belum_terakreditasi','-'),('baik', 'Baik Sekali')])

    #define the akreditation fields from akreditation selection
    akreditation = fields.Selection(string='Akreditasi', selection=select_akreditation)

    #define field to upload docs
    documents = fields.Binary(string='Dokumen Pendukung')

    #define fields for file name of uploaded docuent
    file_name=fields.Char(string='File Name')