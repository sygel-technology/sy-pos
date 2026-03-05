# Copyright 2023 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "POS Session Closing Notes",
    "summary": "Closing session notes from POS to backend.",
    "version": "18.0.1.0.1",
    "category": "POS",
    "website": "https://github.com/sygel-technology/sy-pos",
    "author": "Sygel",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "point_of_sale",
    ],
    "data": [
        "views/pos_session_view.xml",
    ],
}
# TODO: TESTS
