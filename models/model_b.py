from odoo import models

class ModelA(models.TransientModel): # Transient Model: handles temporary data (wizard-style, auto-deleted).
    _name = 'model.b' 

