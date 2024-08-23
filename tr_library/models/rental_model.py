from odoo import models, fields, api



class RentalModel(models.Model):
    _name = 'rental.model'
    _description = 'Rental Model Library'
    _rec_name = 'customer'



    customer = fields.Many2one('res.partner', string="Customer")
    book_id = fields.Many2one('book.model', string="Book")
    longitude = fields.Float(string="Longitude")
    latitude = fields.Float(string="Latittude")
