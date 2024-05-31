# Copyright 2024 Prabakaran
# License OPL-1 (See LICENSE file for full copyright and licensing details).

{
    'name': 'Event Management',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Manage events',
    'description': 'Module to manage events.',
    'depends': ['base'],
    'data': [
        'security/event_security.xml',
        'security/ir.model.access.csv',
        'views/event_management_views.xml',
    ],
    'installable': True,
    'application': True,
}
