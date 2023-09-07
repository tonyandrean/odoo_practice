#import the libraries
from dataclasses import field
from odoo import models, fields

#define class of models survey
class survey_kepuasan(models.Model):
    _name="survey.kepuasan"
    _inherit = ['mail.thread']
    _description="Input Survey Tingkat Kepuasan Dosen"

    kepuasan_bebangaji = fields.Selection(string='Kesempatan mendapatkan beban kerja sesuai dengan keahlian/kompetensi', selection=[('1', 'Baik Sekali'), ('2', 'Baik'),('3','Kurang'),('4','Kurang Sekali')])
    ketersediaan_sop = fields.Selection(string='Ketersediaan SOP untuk menjalankan tugas Tri Dharma Perguruan Tinggi', selection=[('1', 'Baik Sekali'), ('2', 'Baik'),('3','Kurang'),('4','Kurang Sekali')])
    sarpras_pembelajaran = fields.Selection(string='Ketersediaan sarana prasarana pendukung kegiatan pembelajaran', selection=[('1', 'Baik Sekali'), ('2', 'Baik'),('3','Kurang'),('4','Kurang Sekali')])
    sarpras_peneltian = fields.Selection(string='Ketersediaan sarana prasarana pendukung kegiatan penelitian dan pengabdian kepada masyarakat', selection=[('1', 'Baik Sekali'), ('2', 'Baik'),('3','Kurang'),('4','Kurang Sekali')])
    kesempatan_pengembangan_diri = fields.Selection(string='Kesempatan dan fasilitas untuk pengembangan diri : mengikuti kursus, pelatihan, seminar, studi lanjut dll', selection=[('1', 'Baik Sekali'), ('2', 'Baik'),('3','Kurang'),('4','Kurang Sekali')])
    fasilitas_informasi_penelitian = fields.Selection(string='Ketersediaan fasilitas memperoleh informasi dan pelayanan melakukan kegiatan penelitian', selection=[('1', 'Baik Sekali'), ('2', 'Baik'),('3','Kurang'),('4','Kurang Sekali')])
    fasilitas_informasi_pengabdian = fields.Selection(string='Ketersediaan fasilitas memperoleh informasi dan pelayanan melakukan kegiatan pengabdian kepada masyarakat', selection=[('1', 'Baik Sekali'), ('2', 'Baik'),('3','Kurang'),('4','Kurang Sekali')])
    fasilitas_tik = fields.Selection(string='Ketersediaan fasilitas TIK serta dukungan sistem informasi dan komunikasi untuk kemudahan pelayanan pembelajaran, administrasi dan evaluasi', selection=[('1', 'Baik Sekali'), ('2', 'Baik'),('3','Kurang'),('4','Kurang Sekali')])
    pemberian_motivasi = fields.Selection(string='Pemberian motivasi dan bimbingan untuk pencapaian prestasi kerja', selection=[('1', 'Baik Sekali'), ('2', 'Baik'),('3','Kurang'),('4','Kurang Sekali')])
    fasilitas_kenaikan_jabatan = fields.Selection(string='Ketersediaan fasilitas layanan untuk kenaikan jabatan fungsional/pangkat dan kesempatan pengembangan karir manajemen', selection=[('1', 'Baik Sekali'), ('2', 'Baik'),('3','Kurang'),('4','Kurang Sekali')])
    kesempatan_pengembangan_ide = fields.Selection(string='Kesempatan mengembangkan ide/gagasan dan dialog dengan pimpinan', selection=[('1', 'Baik Sekali'), ('2', 'Baik'),('3','Kurang'),('4','Kurang Sekali')])
    pemberian_penghargaan = fields.Selection(string='Pemberian penghargaan atas prestasi kerja yang baik', selection=[('1', 'Baik Sekali'), ('2', 'Baik'),('3','Kurang'),('4','Kurang Sekali')])
    keberadaan_sangsi = fields.Selection(string='Keberadaan sangsi/teguran/peringatan atas pelanggaran kode etik dosen dan peraturan-peraturan lain institusi', selection=[('1', 'Baik Sekali'), ('2', 'Baik'),('3','Kurang'),('4','Kurang Sekali')])
    pemberian_hak = fields.Selection(string='Pemberian hak-hak untuk kesejahteraan atas pelaksanaan tugas rutin.', selection=[('1', 'Baik Sekali'), ('2', 'Baik'),('3','Kurang'),('4','Kurang Sekali')])