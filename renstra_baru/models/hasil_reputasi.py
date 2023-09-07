#import the libraries
from dataclasses import field
from odoo import models, fields, api, _, tools
from odoo.exceptions import Warning ,ValidationError

class hasil_jib(models.Model):
    _name='hasil.jib'
    _description='Hasil bagi jurnal bereputasi'
    _auto = False

    tahun = fields.Char(string='Tahun')
    jumlah_record = fields.Integer(string='Jumlah Jurnal')
    jumlah_dosen = fields.Integer(string='Jumlah Dosen')

    #ir.config_parameter ada di templates.xml, lihat datanya ada di odoo settings>technical>system parameters
    # @api.depends('jumlah_record', 'jumlah_dosen')
    # def get_hasil(self):
    #     for line in self:
    #         line.hasil = line.jumlah_record / line.jumlah_dosen
    #         param = 0
    #         idparam = self.env['ir.config_parameter'].sudo().search([('key', '=', 'jib_' + str(line.tahun))])
    #         if idparam:
    #             param = float(idparam.value)
    #         stat = '1'
    #         if line.hasil >= param:
    #             stat = '1'
    #         else:
    #             stat = '2'
    #         line.status = stat
    #         line.parameter = param

    @api.depends('jumlah_record', 'jumlah_dosen')
    def get_hasil(self):
        for line in self:
            line.hasil = line.jumlah_record / line.jumlah_dosen
            param = 0
            tahun = line.env['rasio.parameter'].sudo().search([], limit=1)  # Mengambil baris pertama dari model rasio.parameter
            if tahun:
                param = getattr(tahun, 'thn_' + line.tahun, 0)  # Mengambil nilai tahun yang sesuai dengan tahun pada model hasil.jib
            stat = '1'
            if line.hasil >= param:
                stat = '1'
            else:
                stat = '2'
            line.status = stat
            line.parameter = param


    hasil = fields.Float(string='Pencapaian', compute='get_hasil')
    status = fields.Selection([
            ('1', 'MEMENUHI'), 
            ('2', 'TIDAK MEMENUHI')
        ], 
        string="Status",
        compute='get_hasil'
    )
    parameter = fields.Float(string='Rasio', compute='get_hasil')

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


# class hasil_reputasi(models.Model):
#     _name='hasil.reputasi'
#     _description='Hasil bagi jurnal bereputasi'

#     jurnal_2021 = fields.Float(string='Tahun 2021', size=4, compute='compute_jurnal_2021')
#     jurnal_2022 = fields.Float(string='Tahun 2022', size=4, compute='compute_jurnal_2022')
#     jurnal_2023 = fields.Float(string='Tahun 2023', size=4, compute='compute_jurnal_2023')
#     jurnal_2024 = fields.Float(string='Tahun 2024', size=4, compute='compute_jurnal_2024')
#     jurnal_2025 = fields.Float(string='Tahun 2025', size=4, compute='compute_jurnal_2025')
#     jurnal_2026 = fields.Float(string='Tahun 2026', size=4, compute='compute_jurnal_2026')
#     #status  = fields.Selection([('memenuhi', 'Memenuhi'), ('tidak', 'Tidak Memenuhi')])


#     #mengambil data hasil jurnal reputasi 2021 dari model hitung.rens
#     @api.depends('jurnal_2021')
#     def compute_jurnal_2021(self):
#         hitung_rens_rec = self.env['hitung.rens'].search([])
#         if hitung_rens_rec:
#             self.jurnal_2021 = hitung_rens_rec[0].result_2021
#         else:
#             self.jurnal_2021 = 0.0

#     #otomatis memperbarui field setiap terjadi perubahan pada field hasil_2021 model hitung.rens
#     @api.onchange('jurnal_2021')
#     def onchange_jurnal_2021(self):
#         hitung_rens_rec = self.env['hitung.rens'].search([])
#         if hitung_rens_rec:
#             self.jurnal_2021 = hitung_rens_rec[0].result_2021
#         else:
#             self.jurnal_2021 = 0.0

#     #mengambil data hasil jurnal reputasi 2022 dari model hitung.rens
#     @api.depends('jurnal_2022')
#     def compute_jurnal_2022(self):
#         hitung_rens_rec = self.env['hitung.rens'].search([])
#         if hitung_rens_rec:
#             self.jurnal_2022 = hitung_rens_rec[0].result_2022
#         else:
#             self.jurnal_2022 = 0.0

#     #otomatis memperbarui field setiap terjadi perubahan pada field hasil_2022 model hitung.rens
#     @api.onchange('jurnal_2022')
#     def onchange_jurnal_2022(self):
#         hitung_rens_rec = self.env['hitung.rens'].search([])
#         if hitung_rens_rec:
#             self.jurnal_2022 = hitung_rens_rec[0].result_2022
#         else:
#             self.jurnal_2022 = 0.0

#     #mengambil data hasil jurnal reputasi 2023 dari model hitung.rens
#     @api.depends('jurnal_2023')
#     def compute_jurnal_2023(self):
#         hitung_rens_rec = self.env['hitung.rens'].search([])
#         if hitung_rens_rec:
#             self.jurnal_2023 = hitung_rens_rec[0].result_2023
#         else:
#             self.jurnal_2023 = 0.0

#     #otomatis memperbarui field setiap terjadi perubahan pada field hasil_2023 model hitung.rens
#     @api.onchange('jurnal_2023')
#     def onchange_jurnal_2023(self):
#         hitung_rens_rec = self.env['hitung.rens'].search([])
#         if hitung_rens_rec:
#             self.jurnal_2023 = hitung_rens_rec[0].result_2023
#         else:
#             self.jurnal_2023 = 0.0

#     #mengambil data hasil jurnal reputasi 2024 dari model hitung.rens
#     @api.depends('jurnal_2024')
#     def compute_jurnal_2024(self):
#         hitung_rens_rec = self.env['hitung.rens'].search([])
#         if hitung_rens_rec:
#             self.jurnal_2024 = hitung_rens_rec[0].result_2024
#         else:
#             self.jurnal_2024 = 0.0

#     #otomatis memperbarui field setiap terjadi perubahan pada field hasil_2024 model hitung.rens
#     @api.onchange('jurnal_2024')
#     def onchange_jurnal_2024(self):
#         hitung_rens_rec = self.env['hitung.rens'].search([])
#         if hitung_rens_rec:
#             self.jurnal_2024 = hitung_rens_rec[0].result_2024
#         else:
#             self.jurnal_2024 = 0.0

#     #mengambil data hasil jurnal reputasi 2025 dari model hitung.rens
#     @api.depends('jurnal_2025')
#     def compute_jurnal_2025(self):
#         hitung_rens_rec = self.env['hitung.rens'].search([])
#         if hitung_rens_rec:
#             self.jurnal_2025 = hitung_rens_rec[0].result_2025
#         else:
#             self.jurnal_2025 = 0.0

#     #otomatis memperbarui field setiap terjadi perubahan pada field hasil_2025 model hitung.rens
#     @api.onchange('jurnal_2025')
#     def onchange_jurnal_2025(self):
#         hitung_rens_rec = self.env['hitung.rens'].search([])
#         if hitung_rens_rec:
#             self.jurnal_2025 = hitung_rens_rec[0].result_2025
#         else:
#             self.jurnal_2025 = 0.0

#     #mengambil data hasil jurnal reputasi 2026 dari model hitung.rens
#     @api.depends('jurnal_2026')
#     def compute_jurnal_2026(self):
#         hitung_rens_rec = self.env['hitung.rens'].search([])
#         if hitung_rens_rec:
#             self.jurnal_2026 = hitung_rens_rec[0].result_2026
#         else:
#             self.jurnal_2026 = 0.0

#     #otomatis memperbarui field setiap terjadi perubahan pada field hasil_2026 model hitung.rens
#     @api.onchange('jurnal_2026')
#     def onchange_jurnal_2026(self):
#         hitung_rens_rec = self.env['hitung.rens'].search([])
#         if hitung_rens_rec:
#             self.jurnal_2026 = hitung_rens_rec[0].result_2026
#         else:
#             self.jurnal_2026 = 0.0

