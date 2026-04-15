# Copyright 2026 Ángel Rivas <angel.rivas@sygel.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "POS Ticket VAT Search",
    "summary": "Adds VAT search to POS orders",
    "version": "18.0.1.0.0",
    "category": "Point of Sale",
    "website": "https://github.com/sygel-technology/sy-pos",
    "author": "Sygel",
    "license": "AGPL-3",
    "depends": [
        "point_of_sale",
    ],
    "assets": {
        "point_of_sale._assets_pos": [
            "sy_pos_order_vat_search/static/src/js/ticket_screen.esm.js",
        ],
    },
    "application": False,
    "installable": True,
}
