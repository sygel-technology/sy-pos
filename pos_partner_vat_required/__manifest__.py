# Copyright 2023 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "POS Partner VAT Required",
    "summary": "VAT required in contacts created on POS.",
    "version": "15.0.1.0.0",
    "category": "POS",
    "website": "https://www.sygel.es",
    "author": "Sygel",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        'point_of_sale',
    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_partner_vat_required/static/src/js/ClientDetailsEdit.js',
        ],
    },
}
