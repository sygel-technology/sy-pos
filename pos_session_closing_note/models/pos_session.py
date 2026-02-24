# Copyright 2023 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, models


class PosSession(models.Model):
    _inherit = "pos.session"

    def _post_cash_details_message(self, state, expected, difference, notes):
        res = super()._post_cash_details_message(state, expected, difference, notes)
        if notes:
            if difference:
                diff = self.currency_id.round(difference)
                if self.currency_id.position == "before":
                    diff = f"{self.currency_id.symbol} {diff}"
                else:
                    diff = f"{diff}{self.currency_id.symbol}"
                notes = _(
                    "Closing difference: %(diff)s\n%(notes)s",
                    state=state,
                    diff=diff,
                    notes=notes,
                )
            self.write({"closing_notes": notes})
        return res
