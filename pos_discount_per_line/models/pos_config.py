# Copyright 2022 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class PosConfig(models.Model):
    _inherit = 'pos.config'

    discount_per_line = fields.Selection(
        selection=[
            ("replace", "Replace"),
            ("sum", "Sum"),
        ],
        string='Discount Per Line',
        required=True,
        default="sum"
    )
