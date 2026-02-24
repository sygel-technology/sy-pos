# Copyright 2026 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.tests.common import TransactionCase


class PosSessionClosingNote(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.session = cls.env.ref("point_of_sale.pos_closed_session_1")

    def test_pos_session_closing_note(self):
        """Call _post_cash_details_message() and check the closing notes"""
        difference = 50
        notes = "notes"
        self.session._post_cash_details_message(
            "Closing", expected=100, difference=difference, notes=notes
        )
        self.assertTrue(self.session.closing_notes)
        self.assertIn(notes, self.session.closing_notes)
        self.assertIn(str(difference), self.session.closing_notes)
