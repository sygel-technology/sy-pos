/* eslint-disable jsdoc/check-tag-names */
/** @odoo-module **/

import {TicketScreen} from "@point_of_sale/app/screens/ticket_screen/ticket_screen";
import {_t} from "@web/core/l10n/translation";
import {patch} from "@web/core/utils/patch";

patch(TicketScreen.prototype, {
    _getSearchFields() {
        const fields = super._getSearchFields(...arguments);

        fields.VAT = {
            repr: (order) => order.partner_id?.vat || "",
            displayName: _t("VAT"),
            modelField: "partner_id.vat",
        };

        return fields;
    },
});
