from odoo import models, fields, api



class BookModel(models.Model):
    _name = 'book.model'
    _description = 'Book Model Library'
    _rec_name = 'internal_reference'


    internal_reference = fields.Char(string='Internal Reference', readonly=True, copy=False)

    book_id = fields.Many2one('tr.library', string='Book')
    isbn = fields.Char(string='ISBN', related='book_id.isbn')
    genre = fields.Char(string='Genre', related='book_id.genre')
    summary = fields.Text(string='Summary', related='book_id.summary')
    author = fields.Char(string='Author', related='book_id.author')
    format = fields.Selection([('paperback', 'Paperback'), ('hardcover', 'Hardcover'),
                               ('audiobook', 'Audiobook'), ('ebook', 'E-Book')], string='Format Book', related='book_id.format')
    language = fields.Selection([('en', 'English'), ('fr', 'France'), ('es', 'Espanol'), ('de', 'Deutsch')],
                                string='Language', related='book_id.language')
    edition = fields.Integer(string='Edition', related='book_id.edition')
    publisher = fields.Char(string='Publisher', related='book_id.publisher')
    publish_date = fields.Date(string='Publish Date', related='book_id.publish_date')
    price = fields.Float(string='Price', related='book_id.price')


    @api.model
    def create(self, vals):
        if not vals.get('internal_reference'):
            seq = self.env['ir.sequence'].next_by_code('book.model')
            vals['internal_reference'] = seq
        return super(BookModel, self).create(vals)