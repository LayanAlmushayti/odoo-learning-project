# A model represents a database table in Odoo, allowing us to define fields and business logic for stored records.
from odoo import models

class ModelA(models.Model): # Define a new Odoo model by creating a Python class that inherits from models.Model
    _name = 'model.a' # The technical name of the model. This name is used by Odoo to create the database table.

