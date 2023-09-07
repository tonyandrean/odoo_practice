#import the libraries
from dataclasses import field
from odoo import models, fields, api, _, tools
from odoo.exceptions import Warning ,ValidationError

class hitung_jib(models.Model):
    _name='hitung.jib'
    _description='Hitung data jurnal bereputasi'
    _auto = False

    tahun = fields.Char(string='Tahun')
    jumlah_record = fields.Integer(string='Jumlah Jurnal')
    jumlah_dosen = fields.Integer(string='Jumlah Dosen')

    @api.depends('jumlah_record', 'jumlah_dosen')
    def get_hasil(self):
        for line in self:
            line.hasil = line.jumlah_record / line.jumlah_dosen

    hasil = fields.Float(string='Hasil', compute='get_hasil')


    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute('''
            CREATE OR REPLACE VIEW %s AS (
                SELECT tahun::integer as id, tahun, count(id)as jumlah_record,
                (SELECT count(id) FROM dosen_dosen)as jumlah_dosen
                FROM jurnal_reputasi 
                GROUP BY tahun
            )''' % (self._table,)
        )

        
# class hitung_rens(models.Model):
#     _name='hitung.rens'
#     _description='Hitung data jurnal bereputasi'

#     jumlah_dosen = fields.Integer(string='Jumlah Dosen', compute='compute_jumlah_dosen')
#     jurnal_2021 = fields.Integer(string='Jurnal Tahun 2021', size=4, compute='compute_jurnal_2021')
#     jurnal_2022 = fields.Integer(string='Jurnal Tahun 2022', size=4, compute='compute_jurnal_2022')
#     jurnal_2023 = fields.Integer(string='Jurnal Tahun 2023', size=4, compute='compute_jurnal_2023')
#     jurnal_2024 = fields.Integer(string='Jurnal Tahun 2024', size=4, compute='compute_jurnal_2024')
#     jurnal_2025 = fields.Integer(string='Jurnal Tahun 2025', size=4, compute='compute_jurnal_2025')
#     jurnal_2026 = fields.Integer(string='Jurnal Tahun 2026', size=4, compute='compute_jurnal_2026')
#     #result = fields.Float(string='Hasil', compute='compute_result', digits=(3,2))
#     result_2021 = fields.Float(string='Hasil 2021', compute='compute_result')
#     result_2022 = fields.Float(string='Hasil 2022', compute='compute_result')
#     result_2023 = fields.Float(string='Hasil 2023', compute='compute_result')
#     result_2024 = fields.Float(string='Hasil 2024', compute='compute_result')
#     result_2025 = fields.Float(string='Hasil 2025', compute='compute_result')
#     result_2026 = fields.Float(string='Hasil 2026', compute='compute_result')

#     #mengambil data jumlah dosen dari model dosen.dosen untuk dihitung
#     @api.depends('jumlah_dosen')
#     def compute_jumlah_dosen(self):
#         dosen_rec = self.env['dosen.dosen'].search([])
#         self.jumlah_dosen = len(dosen_rec)

#     #otomatis memperbarui field setiap terjadi perubahan pada field jumlah_dosen
#     @api.onchange('jumlah_dosen')
#     def onchange_jumlah_dosen(self):
#         dosen_rec = self.env['dosen.dosen'].search([])
#         self.jumlah_dosen = len(dosen_rec)

#     #2021
#     @api.depends('jurnal_2021')
#     def compute_jurnal_2021(self):
#         jurnal_2021_rec = self.env['jurnal.reputasi'].search([('tahun', '=', 2021)])
#         self.jurnal_2021 = len(jurnal_2021_rec)

#     @api.onchange('jurnal_2021')
#     def onchange_jurnal_2021(self):
#         jurnal_2021_rec = self.env['jurnal.reputasi'].search([('tahun', '=', 2021)])
#         self.jurnal_2021 = len(jurnal_2021_rec)

#     #2022
#     @api.depends('jurnal_2022')
#     def compute_jurnal_2022(self):
#         jurnal_2022_rec = self.env['jurnal.reputasi'].search([('tahun', '=', 2022)])
#         self.jurnal_2022 = len(jurnal_2022_rec)

#     @api.onchange('jurnal_2022')
#     def onchange_jurnal_2022(self):
#         jurnal_2022_rec = self.env['jurnal.reputasi'].search([('tahun', '=', 2022)])
#         self.jurnal_2022 = len(jurnal_2022_rec)

#     #2023
#     @api.depends('jurnal_2023')
#     def compute_jurnal_2023(self):
#         jurnal_2023_rec = self.env['jurnal.reputasi'].search([('tahun', '=', 2023)])
#         self.jurnal_2023 = len(jurnal_2023_rec)

#     @api.onchange('jurnal_2023')
#     def onchange_jurnal_2023(self):
#         jurnal_2023_rec = self.env['jurnal.reputasi'].search([('tahun', '=', 2023)])
#         self.jurnal_2023 = len(jurnal_2023_rec)

#     #2024
#     @api.depends('jurnal_2024')
#     def compute_jurnal_2024(self):
#         jurnal_2024_rec = self.env['jurnal.reputasi'].search([('tahun', '=', 2024)])
#         self.jurnal_2024 = len(jurnal_2024_rec)

#     @api.onchange('jurnal_2024')
#     def onchange_jurnal_2024(self):
#         jurnal_2024_rec = self.env['jurnal.reputasi'].search([('tahun', '=', 2024)])
#         self.jurnal_2024 = len(jurnal_2024_rec)

#     #2025
#     @api.depends('jurnal_2025')
#     def compute_jurnal_2025(self):
#         jurnal_2025_rec = self.env['jurnal.reputasi'].search([('tahun', '=', 2025)])
#         self.jurnal_2025 = len(jurnal_2025_rec)

#     @api.onchange('jurnal_2025')
#     def onchange_jurnal_2025(self):
#         jurnal_2025_rec = self.env['jurnal.reputasi'].search([('tahun', '=', 2025)])
#         self.jurnal_2025 = len(jurnal_2025_rec)

#     #2026
#     @api.depends('jurnal_2026')
#     def compute_jurnal_2026(self):
#         jurnal_2026_rec = self.env['jurnal.reputasi'].search([('tahun', '=', 2026)])
#         self.jurnal_2026 = len(jurnal_2026_rec)

#     @api.onchange('jurnal_2026')
#     def onchange_jurnal_2026(self):
#         jurnal_2026_rec = self.env['jurnal.reputasi'].search([('tahun', '=', 2026)])
#         self.jurnal_2026 = len(jurnal_2026_rec)
   
#     @api.depends('jumlah_dosen', 'jurnal_2021', 'jurnal_2022', 'jurnal_2023', 'jurnal_2024', 'jurnal_2025', 'jurnal_2026')
#     def compute_result(self):
#         for rec in self:
#             if rec.jurnal_2021 == 0:
#                 rec.result_2021 = 0.0
#             else:
#                 rec.result_2021 = rec.jumlah_dosen / rec.jurnal_2021
            
#             if rec.jurnal_2022 == 0:
#                 rec.result_2022 = 0.0
#             else:
#                 rec.result_2022 = rec.jumlah_dosen / rec.jurnal_2022

#             if rec.jurnal_2023 == 0:
#                 rec.result_2023 = 0.0
#             else:
#                 rec.result_2023 = rec.jumlah_dosen / rec.jurnal_2023

#             if rec.jurnal_2024 == 0:
#                 rec.result_2024 = 0.0
#             else:
#                 rec.result_2024 = rec.jumlah_dosen / rec.jurnal_2024

#             if rec.jurnal_2025 == 0:
#                 rec.result_2025 = 0.0
#             else:
#                 rec.result_2025 = rec.jumlah_dosen / rec.jurnal_2025

#             if rec.jurnal_2026 == 0:
#                 rec.result_2026 = 0.0
#             else:
#                 rec.result_2026 = rec.jumlah_dosen / rec.jurnal_2026
    
#     @api.onchange('jumlah_dosen', 'jurnal_2021', 'jurnal_2022', 'jurnal_2023', 'jurnal_2024', 'jurnal_2025', 'jurnal_2026')
#     def onchange_compute_result(self):
#         if self.jurnal_2021 == 0:
#             self.result_2021 = 0.0
#         else:
#             self.result_2021 = self.jumlah_dosen / self.jurnal_2021

#         if self.jurnal_2022 == 0:
#             self.result_2022 = 0.0
#         else:
#             self.result_2022 = self.jumlah_dosen / self.jurnal_2022

#         if self.jurnal_2023 == 0:
#             self.result_2023 = 0.0
#         else:
#             self.result_2023 = self.jumlah_dosen / self.jurnal_2023

#         if self.jurnal_2024 == 0:
#             self.result_2024 = 0.0
#         else:
#             self.result_2024 = self.jumlah_dosen / self.jurnal_2024

#         if self.jurnal_2025 == 0:
#             self.result_2025 = 0.0
#         else:
#             self.result_2025 = self.jumlah_dosen / self.jurnal_2025

#         if self.jurnal_2026 == 0:
#             self.result_2026 = 0.0
#         else:
#             self.result_2026 = self.jumlah_dosen / self.jurnal_2026

