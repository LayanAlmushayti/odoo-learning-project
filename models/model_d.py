from odoo import models

class ModelA(models.Model):
    _name = 'model.d' 
    _log_access = False # disables automatic create/write timestamp fields

