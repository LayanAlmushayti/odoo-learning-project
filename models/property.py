from odoo import models , fields , api
from odoo.exceptions import ValidationError


class Propert(models.Model):
    _name = 'property'

    name = fields.Char(required= 1, default="New" , size= 7) # Name is required with "New" as its default (max 7 chars).
    description = fields.Char()
    postcode = fields.Char(required= 1)
    date_availability = fields.Date()
    expected_price = fields.Float(digits=(0,5)) # limits the float field to 5 decimal places
    selling_price = fields.Float ()
    bedrooms = fields.Integer(required= 1)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
        ('north' , 'North'),
        ('south' , 'South'),
        ('east' , 'East'),
        ('west' , 'West'),
    ])


# This constraint ensures that the 'bedrooms' field is always greater than zero; 
# if the value is 0, it raises a ValidationError to prevent saving invalid data.
    @api.constrains('bedrooms')
    def _check_bedrooms_greater_zero(self):
        for rec in self:
            if rec.bedrooms == 0:
                raise ValidationError('please add valid number of bedrooms')


# Adds an SQL constraint to validate data:
# - unique_name: the constraint name
# - unique("name"): ensures the 'name' field is unique in the database
# - 'this name is exist': error message when duplicate data is entered
    _sql_constraints = [
    ('unique_name', 'unique("name")', 'this name is exist'),
]