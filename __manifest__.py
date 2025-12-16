# This file (__manifest__.py) defines the basic information and configuration
# for the Odoo module. It tells Odoo the module's name, author, category,
# version, dependencies, and which data files (XML) should be loaded.
# The "application" flag makes the module appear in the Apps menu.

{
    'name': 'App One',
    'author': 'Layan Khalid',
    'category': 'Custom',
    'version': '17.0.0.1.0',
    'depends': ['base',
                ],
    'data': [
        # ضيفي XML files هنا لاحقاً
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/property_view.xml',
        'views/owner_view.xml',
        'views/tag_view.xml',
    ],
    'assets' : {
        'web.assets_backend' : ['app_one\static\src\css\property.css']
    },
    'application': True,
}
