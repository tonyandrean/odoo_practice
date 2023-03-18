from dataclasses import field
from odoo import models, fields

class renstra_fakultas(models.Model):

    select_faculty=([('komputer','Fakultas Ilmu Komputer'),('teknik','Fakultas Teknik'),('ekonomi','Fakultas Ekonomi dan Bisnis'),
        ('budaya','Fakultas Ilmu Budaya')])

    #define the faculty fields from 
    faculty = fields.Selection(string='Fakultas', selection=select_faculty)