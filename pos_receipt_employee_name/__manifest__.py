# Copyright 2024 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "POS Receipt Employee Name",
    "summary": "Select employee name to be shown in POS receipts",
    "category": "POS",
    "website": "https://github.com/sygel-technology/sy-pos",
    "author": "Sygel",
    "license": "AGPL-3",
    "version": "15.0.1.0.0",
    "depends": [
        "pos_hr",
    ],
    "data": [
        "views/hr_employee_views.xml",
    ],
    "assets": {
        "point_of_sale.assets": [
            "pos_receipt_employee_name/static/src/js/models.js",
        ],
    },
}
