from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError



class TrainLibrary(models.Model):
    _name = 'tr.library'
    _description = 'Module Training Odoo Library'



    name = fields.Char(string='Name')
    active = fields.Boolean(default=True)
    isbn = fields.Char(string='ISBN')
    genre = fields.Char(string='Genre')
    summary = fields.Text(string='Summary')
    author = fields.Char(string='Author')
    format = fields.Selection([('paperback', 'Paperback'), ('hardcover', 'Hardcover'),
                              ('audiobook', 'Audiobook'), ('ebook', 'E-Book')], string='Format Book')
    language = fields.Selection([('en', 'English'), ('fr', 'France'), ('es', 'Espanol'), ('de', 'Deutsch')], string='Language')
    edition = fields.Integer()
    publisher = fields.Char(string='Publisher')
    publish_date = fields.Date(string='Publish Date')
    price = fields.Float(string='Price')


    @api.onchange('isbn')
    def check_isbn_length(self):
        for rec in self:
            if len(rec.isbn) != 13:
                raise ValidationError('ISBN is not the correct length')