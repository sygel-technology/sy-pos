# Copyright 2026 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    discount_per_line = fields.Selection(
        related="pos_config_id.discount_per_line",
        readonly=False,
        required=True,
    )
