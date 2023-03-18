from dataclasses import field
from odoo import models, fields,api
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning
class renstra_kelulusan(models.Model):
    _name="renstra.kelulusan.mhs"
    _description="Modul for input graduation data"

    #create full name field
    name=fields.Char('Nama Lengkap',required=True)

    #Create NIM fields
    nim=fields.Char('NIM',required=True)

    #Create tahun masuk fields
    tahun_masuk = fields.Integer(string="Tahun Masuk",required=True)

    #create fields of IPK
    ipk = fields.Float(string='IPK', digits=(4, 2))

    #create fields of state
    state = fields.Selection(string='Status Kelulusan', selection=[('L', 'Lulus'), ('BL', 'Belum Lulus')])

    #create fields for lama study
    lama_study = fields.Integer(string='Lama Study',required=True)
    rata_study = fields.Float(string='Rata Rata Lama Study', digits=(4,1))

    #create jurusan selection field
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
    jurusan = fields.Selection(string='Program Study', selection=jurusan_list)
    
    # @api.depends("lama_study")
    # def _Testmean(self):
    #     for record in self:
    #         record.rata_study=mean(record.lama_study)