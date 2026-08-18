# -*- coding: utf-8 -*-
{
    'name': 'BugFix - Defaults',
    'version': '17.0.0.0.2',
    'summary': 'Studio-configured ir.default records (427) across the system',
    'author': 'Jinasena Agricultural Machinery (Pvt) Ltd.',
    'category': 'Extra Tools',
    'license': 'LGPL-3',
    # Do NOT depend on studio_customization — Odoo SH does not ship a manifest for it.
    'depends': ['base_setup'],
    'data': ['data/defaults.xml'],
    'installable': True,
    'auto_install': False,
    'application': True,
}
