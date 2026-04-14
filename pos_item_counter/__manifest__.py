# Copyright 2023 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "POS Item Counter",
    "summary": "Show number of items in POS.",
    "version": "18.0.1.0.1",
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
        "point_of_sale._assets_pos": [
            "pos_item_counter/static/src/js/ItemCounter.esm.js",
            "pos_item_counter/static/src/xml/ItemCounter.xml",
        ]
    },
}
