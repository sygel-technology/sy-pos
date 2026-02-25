# Copyright 2023 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class UomUom(models.Model):
    _inherit = "uom.uom"

    is_units = fields.Boolean(compute="_compute_is_units", readonly=True, store=True)

    def _compute_is_units(self):
        units_uom_id = self.env.ref("uom.product_uom_unit")
        for sel in self:
            is_units = False
            if units_uom_id and sel.id == units_uom_id.id:
                is_units = True
            sel.is_units = is_units

    def _load_pos_data_fields(self, config_id):
        res = super()._load_pos_data_fields(config_id)
        res.append("is_units")
        return res
