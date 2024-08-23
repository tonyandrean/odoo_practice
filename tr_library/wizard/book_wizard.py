from odoo import models, fields, api



class BookWizard(models.TransientModel):
    _name = 'book.wizard'
    _description = 'Book Wizard'



    book_id = fields.Many2one('book.model', string='Book')
    customer_ids = fields.Many2many('res.partner', string='Customer')


    def create_book(self):
        return {'type': 'ir.actions.client',
                'tag': 'reload'}