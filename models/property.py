from odoo import models , fields , api
from odoo.exceptions import ValidationError


class Propert(models.Model):
    _name = 'property'

    name = fields.Char(required= 1, default="New" , size= 7) # Name is required with "New" as its default (max 7 chars).
    description = fields.Char()
    postcode = fields.Char(required= 1)
    date_availability = fields.Date()
    expected_price = fields.Float() # digits=(0,5) limits the float field to 5 decimal places
    selling_price = fields.Float ()
    diff = fields.Float(compute="_compute_diff" , store = 1) #readonly= 0, if i want the user to be able to edit, not only read it
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
    #Relational Fields
    owner_id = fields.Many2one('owner')
    tag_ids = fields.Many2many('tag')

    owner_address = fields.Char(related = 'owner_id.address') # u can use readonly = 0 if you want the user to edit the val from the prop form
    owner_phone = fields.Char(related = 'owner_id.phone') # if u want to store this field u can use store = 1

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





    state = fields.Selection([
        ('draft' , 'Draft'),
        ('pending' , 'Pending'),
        ('sold' , 'Sold'),
    ], default= 'draft')


# Any compute method must have @api.depends to know when to recalculate

#If the user changes expected_price → recalculate total_profit
#If the user changes selling_price → recalculate total_profit
#Odoo will automatically call the compute function again without you doing anything.
    @api.depends('expected_price', 'selling_price' ,'owner_id.phone') # Runs compute again if price fields or owner_id.phone is updated
    def _compute_diff(self):
        for rec in self:
            rec.diff = rec.expected_price - rec.selling_price


    @api.onchange('expected_price') # Runs only in the UI to update fields instantly when expected_price changes
    def _onchange_expected_price(self):
        print('inside onchange')
        return {
            'warning' : {'title': 'warning' , 'message' : 'negative value', 'type':'notification'}
        }

    #CRUD
    #overwrite create function
    @api.model_create_multi
    def create(self , vals):
        res = super(Propert, self).create(vals) #or super(Propert, self).create(vals)
        #logic
        print("inside create method")
        return res
    
    #read
    @api.model
    def _search(self, domain, offset=0, limit=None, order=None, access_rights_uid=None):
        res= super()._search(domain, offset, limit, order, access_rights_uid)
        #logic
        print("inside search method")
        return res
    
    #update
    def write(self, vals):
        res = super().write(vals)
        #logic
        print("inside write method")
        return res
    
    #delete
    def unlink(self):
        res = super(Propert , self).unlink()
        #logic
        print("inside delete method")
        return res
    
    def action_draft(self):
        for rec in self:
            print('inside draft action')
            rec.state = 'draft'

    def action_pending(self):
        for rec in self:
            print('inside pending action')
            rec.state = 'pending'

    def action_sold(self):
        for rec in self:
            print('inside sold action')
            rec.state = 'sold'