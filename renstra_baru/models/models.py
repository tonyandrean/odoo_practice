# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class rrenstra_ft(models.Model):
#     _name = 'rrenstra_ft.rrenstra_ft'
#     _description = 'rrenstra_ft.rrenstra_ft'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
