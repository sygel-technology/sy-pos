# Copyright 2026 Ángel Rivas <angel.rivas@sygel.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "POS Order Line Discount Display",
    "summary": "Improve display of price and discounts in POS order lines",
    "version": "18.0.1.0.0",
    "category": "Point of Sale",
    "website": "https://github.com/sygel-technology/sy-pos",
    "author": "Sygel",
    "license": "AGPL-3",
    "depends": ["point_of_sale"],
    "assets": {
        "point_of_sale._assets_pos": [
            "sy_pos_order_line_discount_display/static/src/js/pos_order_line.esm.js",
            "sy_pos_order_line_discount_display/static/src/js/orderline_component_patch.esm.js",
            "sy_pos_order_line_discount_display/static/src/xml/pos_order_line_discount.xml",
        ],
    },
    "application": False,
    "installable": True,
}
