from odoo import models, fields, api



class Project(models.Model):
    _inherit = 'project.project'



    book_id = fields.Many2one('book.model', string='Book Rent Reference')