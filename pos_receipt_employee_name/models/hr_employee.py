# Copyright 2026 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class HrEmployee(models.AbstractModel):
    _inherit = "hr.employee"

    def _load_pos_data_fields(self, config_id):
        res = super()._load_pos_data_fields(config_id)
        res += ["pos_receipt_name"]
        return res
