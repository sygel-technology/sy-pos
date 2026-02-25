# Copyright 2023 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "POS Number Items",
    "summary": "Show number of items in POS.",
    "version": "15.0.1.0.0",
    "category": "Custom",
    "website": "https://github.com/sygel-technology/sy-pos",
    "author": "Sygel",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "point_of_sale",
    ],
    "assets": {
        "point_of_sale.assets": [
            "pos_items_counter/static/src/js/ItemsCounter.js",
        ],
        "web.assets_qweb": [
            "pos_items_counter/static/src/xml/ItemsCounter.xml",
            "pos_items_counter/static/src/xml/OrderSummary.xml",
        ],
    },
}
