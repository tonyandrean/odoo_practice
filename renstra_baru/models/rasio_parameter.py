#import the libraries
from dataclasses import field
from odoo import models, fields, api, _, tools
from odoo.exceptions import Warning ,ValidationError

class rasio_parameter(models.Model):
    _name='rasio.parameter'
    _inherit = ['mail.thread']
    _description='rasio untuk hasil bagi jurnal pertahun per dosen'

    indikator = fields.Selection(string='Indikator Kinerja Utama', selection=[
                                ('jib', 'Jurnal internasional bereputasi'), 
                                ('ji', 'Jurnal Internasional'), 
                                ('jnt', 'Jurnal nasional terakreditasi')])
    thn_2021 = fields.Float(string='2021')
    thn_2022 = fields.Float(string='2022')
    thn_2023 = fields.Float(string='2023')
    thn_2024 = fields.Float(string='2024')
    thn_2025 = fields.Float(string='2025')
    thn_2026 = fields.Float(string='2026')