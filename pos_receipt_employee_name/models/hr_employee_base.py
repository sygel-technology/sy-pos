# Copyright 2024 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class HrEmployeeBase(models.AbstractModel):
    _inherit = 'hr.employee.base'

    pos_receipt_name = fields.Char(
        string="POS Receipt Name",
        help=(
            "Employee's name that is shown in POS receipts when this employee is active."
        ),
    )
