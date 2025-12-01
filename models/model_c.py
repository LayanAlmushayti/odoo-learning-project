from odoo import models

class ModelA(models.AbstractModel): # Abstract model used to share logic; no database table is created.

    _name = 'model.c' 

