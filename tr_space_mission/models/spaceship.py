from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError



class Spaceship(models.Model):
    _name = 'tr.spaceship'
    _description = 'Module Training Odoo Space Mission'



    name = fields.Char("Name")
    active = fields.Boolean(default=True)
    type = fields.Selection([('freighter', 'Freighter'), ('transport', 'Transport'), ('scout_ship', 'Scout Ship'),
                             ('fighter', 'Fighter')], string="Type")
    model = fields.Char(string="Model")
    build_date = fields.Date(string="Build Date")
    captain = fields.Char(string="Captain")
    required_crew = fields.Integer(string="Required Crew")
    length = fields.Float(string="Length")
    width = fields.Float(string="Width")
    height = fields.Float(string="Height")
    engine_number = fields.Char(string="Engine Number")
    fuel_type = fields.Selection([('solid_fuel', 'Solid Fuel'), ('liquid_fuel', 'Liquid Fuel')], string="Fuel Type")
    total_dimension = fields.Float(string="Total Dimension Spaceship", compute='_compute_total_dimension')
    total_crew = fields.Integer(string="Total Crew", compute='_compute_total_crew')


    @api.constrains('width', 'length')
    def check_width(self):
        for rec in self:
            if rec.width >= rec.length:
                raise UserError("Width cannot larger than length")

    @api.depends('length', 'width', 'height')
    def _compute_total_dimension(self):
        for rec in self:
            if rec.length and rec.width:
                rec.total_dimension = rec.length + rec.width + rec.height