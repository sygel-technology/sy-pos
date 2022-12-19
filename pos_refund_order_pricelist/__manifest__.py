# Copyright 2022 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "POS Refund Order Pricelist",
    "summary": "POS Order Preclist in refund ordersß",
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
    'assets': {
        'point_of_sale.assets': [
            'pos_refund_order_pricelist/static/src/js/TicketScreen.js',
        ],
    },
}
