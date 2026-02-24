# Copyright 2023 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, _


class PosSession(models.Model):
    _inherit = "pos.session"

    closing_notes = fields.Text(
        string="Closing Notes",
        readonly=True
    )

    def _post_cash_details_message(self, state, difference, notes):
        super()._post_cash_details_message(state, difference, notes)
        if notes:
            if difference:
                notes = _("{} difference: {}{}{}\n{}").format(
                    state,
                    self.currency_id.symbol + ' ' if self.currency_id.position == 'before' else '',+
                    self.currency_id.round(difference),
                    self.currency_id.symbol if self.currency_id.position == 'after' else '',
                    notes
                )
            self.write({
                'closing_notes': notes
            })
