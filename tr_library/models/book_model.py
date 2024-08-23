from odoo import models, fields, api



class BookModel(models.Model):
    _name = 'book.model'
    _description = 'Book Model Library'
    _rec_name = 'book'


    book = fields.Char(string='Book')