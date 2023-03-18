#import the libraries
from dataclasses import field
from odoo import models, fields

#define class of models survey
class survey_kepuasan_tenagapendidikan(models.Model):
    _name="survey.kepuasan.tenagakependidikan"
    _description="Input Survey Tingkat Kepuasan Tenaga Kependidikan"

    kepuasan_bebankerja = fields.Selection(string='kesempatan mendapatkan beban kerja sesuai dengan keahlian/kompetensi', selection=[('1', '1'), ('2', '2'),('3','3'),('4','4')])
    ketersediaan_sop = fields.Selection(string='Ketersediaan SOP untuk menjalankan tugas administrasi', selection=[('1', '1'), ('2', '2'),('3','3'),('4','4')])
    kesempatan_pengembangan_diri = fields.Selection(string='Kesempatan dan fasilitas untuk pengembangan diri : mengikuti kursus, pelatihan, seminar, studi lanjut dll', selection=[('1', '1'), ('2', '2'),('3','3'),('4','4')])
    fasilitas_tik = fields.Selection(string='Ketersediaan fasilitas TIK serta dukungan sistem informasi dan komunikasi untuk kemudahan pelayanan pembelajaran, administrasi dan evaluasi', selection=[('1', '1'), ('2', '2'),('3','3'),('4','4')])
    pemberian_motivasi = fields.Selection(string='Pemberian motivasi dan bimbingan untuk pencapaian prestasi kerja', selection=[('1', '1'), ('2', '2'),('3','3'),('4','4')])
    fasilitas_kenaikan_jabatan = fields.Selection(string='Ketersediaan fasilitas layanan untuk kenaikan jabatan fungsional/pangkat dan kesempatan pengembangan karir manajemen', selection=[('1', '1'), ('2', '2'),('3','3'),('4','4')])
    kesempatan_pengembangan_ide = fields.Selection(string='Kesempatan mengembangkan ide/gagasan dan dialog dengan pimpinan', selection=[('1', '1'), ('2', '2'),('3','3'),('4','4')])
    pemberian_penghargaan = fields.Selection(string='Pemberian penghargaan atas prestasi kerja yang baik', selection=[('1', '1'), ('2', '2'),('3','3'),('4','4')])
    keberadaan_sangsi = fields.Selection(string='Keberadaan sangsi/teguran/peringatan atas pelanggaran kode etik dosen dan peraturan-peraturan lain institusi', selection=[('1', '1'), ('2', '2'),('3','3'),('4','4')])
    pemberian_hak = fields.Selection(string='Pemberian hak-hak untuk kesejahteraan atas pelaksanaan tugas rutin.', selection=[('1', '1'), ('2', '2'),('3','3'),('4','4')])


    
