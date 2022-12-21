# Copyright 2022 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "POS Discount Per Line",
    "summary": "Apply general discounton each line",
    "version": "15.0.1.0.0",
    "category": "Point of Sale",
    "website": "https://www.sygel.es",
    "author": "Sygel, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "point_of_sale",
    ],
    'data': [
        'views/pos_config_view.xml'
    ],
    'assets': {
        'web.assets_qweb': [
            'pos_discount_per_line/static/src/xml/**/*',
        ],
        'point_of_sale.assets': [
            'pos_discount_per_line/static/src/js/**/*',
        ],
    },
}
