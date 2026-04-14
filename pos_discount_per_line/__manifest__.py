# Copyright 2022 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "POS Discount Per Line",
    "summary": "Apply general discount on each line",
    "version": "18.0.1.0.1",
    "category": "Point of Sale",
    "website": "https://github.com/sygel-technology/sy-pos",
    "author": "Sygel",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "pos_discount",
    ],
    "data": ["views/pos_config_view.xml"],
    "assets": {
        "point_of_sale._assets_pos": [
            "pos_discount_per_line/static/src/control_buttons/control_buttons.xml",
            "pos_discount_per_line/static/src/control_buttons/control_buttons.esm.js",
            "pos_discount_per_line/static/src/number_popup/number_popup.xml",
            "pos_discount_per_line/static/src/number_popup/number_popup.esm.js",
        ],
    },
}
