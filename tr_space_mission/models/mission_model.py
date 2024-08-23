from odoo import models, fields, api



class MissionModel(models.Model):
    _name = 'mission.model'
    _description = 'Mission Model Spaceship'
    _rec_name = 'mission'


    project_line = fields.One2many('project.project', inverse_name='mission_id')

    mission = fields.Char(string='Mission')
    space_id = fields.Many2one('tr.spaceship', string='Spaceship Name')
    captain = fields.Many2one('res.partner')