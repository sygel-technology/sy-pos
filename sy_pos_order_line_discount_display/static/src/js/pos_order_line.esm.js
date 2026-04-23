/* eslint-disable jsdoc/check-tag-names */
/** @odoo-module **/

import {PosOrderline} from "@point_of_sale/app/models/pos_order_line";
import {accountTaxHelpers} from "@account/helpers/account_tax";
import {formatCurrency} from "@point_of_sale/app/models/utils/currency";
import {patch} from "@web/core/utils/patch";

patch(PosOrderline.prototype, {
    getOriginalTaxedUnitPrice() {
        const product = this.get_product();
        const company = this.company;

        const baseLine = accountTaxHelpers.prepare_base_line_for_taxes_computation(
            this,
            this.prepareBaseLineForTaxesComputationExtraValues({
                price_unit: product.lst_price,
                quantity: 1,
                tax_ids: product.taxes_id,
                discount: 0.0,
            })
        );

        accountTaxHelpers.add_tax_details_in_base_line(baseLine, company);
        accountTaxHelpers.round_base_lines_tax_details([baseLine], company);

        if (this.config.iface_tax_included === "total") {
            return baseLine.tax_details.total_included_currency;
        }
        return baseLine.tax_details.total_excluded_currency;
    },

    getPricelistDiscountPercent() {
        const original = this.getOriginalTaxedUnitPrice();
        const priceAfterPricelist = this.getUnitDisplayPriceBeforeDiscount();

        if (original > 0 && original > priceAfterPricelist) {
            return Math.round((1 - priceAfterPricelist / original) * 100);
        }
        return 0;
    },

    getDisplayData() {
        const data = super.getDisplayData(...arguments);

        const original = this.getOriginalTaxedUnitPrice();
        const priceAfterPricelist = this.getUnitDisplayPriceBeforeDiscount();
        const pricelistPerc = this.getPricelistDiscountPercent();
        const manualPerc = this.get_discount();

        const hasManualDiscount = manualPerc > 0;
        const hasPricelistDiscount = pricelistPerc > 0;

        if (hasManualDiscount || hasPricelistDiscount) {
            data.oldUnitPrice = formatCurrency(original, this.currency);
        }

        data.pricelistDiscountPercent = pricelistPerc ? String(pricelistPerc) : "";
        data.manualDiscountPercent = manualPerc ? String(manualPerc) : "";
        data.priceAfterPricelist = formatCurrency(priceAfterPricelist, this.currency);

        return data;
    },
});
