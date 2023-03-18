#import the libraries
from dataclasses import field
from odoo import models, fields,api
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning

#define the class of akreditasi database
class akreditasi_banpt(models.Model):
    #define the models name and the description
    _name='akreditasi.ban.pt'
    _description='Input data for acreditaion BAN PT'

    #define periode fields
    periode = fields.Char(string='Periode')

    #define the kode jurusan fields
    kode = fields.Char(string='Kode Jurusan')

    #define nama_jurusan fields
    nama_jurusan = fields.Char(string='Nama Jurusan')#unused
    jurusan_list = [('informatika', 'Teknik Informatika - S1/Bachelor of Informatics'),
                    ('informasi', 'Sistem Informasi - S1/Bachelor of Information System'),
                    ('maninfor1', 'Manajemen Informatika - S1/'),
                    ('dkv', 'Desain Komunikasi Visual - S1/Bachelor of Visual Communication Design'),
                    ('ilkom', 'Ilmu Komunikasi - S1/Bachelor of Communication Science'),
                    ('ftv', 'Film dan Televisi - SST/Bachelor of Film and Television'),
                    ('animasi', 'Animasi - SST/Bachelor of Animation'),
                    ('maninford3', 'Manajemen Informatika - D3/Diploma of Software Application Engineering'),
                    ('informatikad3', 'Teknik Informatika - D3/Diploma of Information Technology'),
                    ('komakun', 'Komputerisasi Akuntansi - D3/'),
                    ('broad', 'Broadcasting - D3/Diploma of Broadcast Journalism'),
                    ('manajemen', 'Manajemen - S1/Bachelor of Management'),
                    ('akuntansi', 'Akuntansi - S1/Bachelor of Accounting'),
                    ('akuntand3', 'Akuntansi - D3/'),
                    ('inggris', 'Bahasa Inggris - S1/Bachelor of English Language'),
                    ('jepang', 'Sastra Jepang - S1/Bachelor of Japanese Language'),
                    ('hotel', 'Pengelolaan Perhotelan - S.Tr./Hotel Management'),
                    ('jepangd3', 'Bahasa Jepang - D3/'),
                    ('kesmas', 'Kesehatan Masyarakat - S1/Bachelor of Public Health'),
                    ('kesling', 'Kesehatan Lingkungan - S1/Bachelor of Enviromental Health'),
                    ('rmik', 'Rekam Medik & Info. Kes. - D3/Diploma of Medical Record'),
                    ('sikediri', 'Sistem Informasi Kampus Kediri - S1/Information System Kediri Campus'),
                    ('mkom', 'Magister Teknik Informatika - S2/Master of Computer Science - S2'),
                    ('mm', 'Magister Manajemen - S2/Master of Management - S2'),
                    ('doktor', 'Program Doktor Ilmu Komputer - S3/Doctor of Computer Science'),
                    ('elektro', 'Teknik Elektro - S1/Bachelor of Electrical Engineering'),
                    ('industri', 'Teknik Industri - S1/Bachelor of Industrial Engineering'),
                    ('biomedis', 'Teknik Biomedis - S1/Bachelor of Biomedical Engineering')]
    jurusan = fields.Selection(string='Nama Jurusan', selection=jurusan_list)



    #define faculty selection
    select_faculty=[('ft', 'Teknik/Engineering'),
                    ('fik', 'Ilmu Komputer/Computer Science'),
                    ('fkes', 'Kesehatan/Health Science'),
                    ('fib', 'Ilmu Budaya/Humanity'),
                    ('feb', 'Ekonomi & Bisnis/Economics & Business')]


    #define the faculty fields from 
    faculty = fields.Selection(string='Fakultas', selection=select_faculty)

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
    file_name=fields.Char(string='FIle Name')

    #define fields for user_id
    
    user_id = fields.Many2one(
        comodel_name='renstra.koordinator',
        string='user ID',
        ondelete='restrict')
        
    #unused
    jurusan_fasilkom=([('a11','A11'),('a12','A12'),('a13','A13'),('a14','A14'),('a15','A15'),('a16','A16'),('a17','A17'),
    ('a21','A21'),('a22','A22'),('a23','A23'),('a24','A24')])
    jurusan_feb=([('b11','B11'),('b12','B12'),('b21','B21')])
    jurusan_ft = [('tek_el', 'E11'),
                ('tek_ind', 'E12'),
                ('tek_bio', 'E13')]


    code=[('ti', 'A11'), ('si', 'A12'), ('mi', 'A13'), ('dkv', 'A14'), ('ilkom', 'A15'), ('ftv', 'A16'),
                ('animasi', 'A17'), ('manajinf', 'A21'), ('tekinf', 'A22'), ('komakun', 'A23'), 
                ('broadcast', 'A24'), ('manajemen', 'B11'), ('akuntansi', 'B12'), ('akuntan', 'B21'), 
                ('sasing', 'C11'), ('sasjep', 'C12'), ('hotel', 'C13'), ('sj', 'C22'), ('kesmas', 'D11'), 
                ('kesling', 'D12'), ('rmik', 'D22'), ('sik', 'F12'), ('mti', 'P31'), ('mm', 'P32'), 
                ('doktor', 'P41'), ('tek_el', 'E11'), ('tek_ind', 'E12'), ('tek_bio', 'E13')]

    feb = fields.Selection(string='Jurusan FEB', selection=jurusan_feb)
    fik = fields.Selection(string='Jurusan FIK', selection=jurusan_fasilkom)
    kode_jurusan = fields.Selection(string='Kode Jurusan', selection=code)
    state = fields.Selection(string='Status', selection=[('draft', 'Draft'),('done','Done')],default='draft',required=True)
      #chage status bar if mark as done
    # @api.onchange('state')
    def set_to_ready_upload(self):
        if self.state == 'draft':
            self.write({
                'state': 'done'
            })
            return{
                'effect':{
                    'fadeout':'slow',
                    'message':'marked as done',
                    'type':'rainbow_man'
                }
            }
        else:
            raise UserError('Status bukan draft')
