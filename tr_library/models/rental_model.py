from odoo import models, fields, api



class RentalModel(models.Model):
    _name = 'rental.model'
    _description = 'Rental Model Library'
    _rec_name = 'customer_id'



    customer_id = fields.Many2one('res.partner', string='Customer')
    book_id = fields.Many2one('book.model', string='Book Reference')
    longitude = fields.Float(string='Longitude')
    latitude = fields.Float(string='Latittude')
