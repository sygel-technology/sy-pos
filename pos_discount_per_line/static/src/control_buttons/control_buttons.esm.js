import {ControlButtons} from "@point_of_sale/app/screens/product_screen/control_buttons/control_buttons";
import {NumberPopupDPL} from "@pos_discount_per_line/number_popup/number_popup.esm";
import {_t} from "@web/core/l10n/translation";
import {patch} from "@web/core/utils/patch";

patch(ControlButtons.prototype, {
    async clickDiscountPerLine() {
        this.dialog.add(NumberPopupDPL, {
            title: _t("Discount Percent Per Line"),
            startingValue: this.pos.config.discount_pc,
            discountPerLineMethod: this.pos.config.discount_per_line,
            getPayload: (num) => {
                const discPolicy = document.getElementById("disc_policy").value;
                const val = Math.max(
                    0,
                    Math.min(100, this.env.utils.parseValidFloat(num.toString()))
                );
                this.apply_discount_per_line(val, discPolicy);
            },
        });
    },
    async apply_discount_per_line(pc, discPolicy) {
        const order = this.pos.get_order();
        const lines = order.get_orderlines();
        const product = this.pos.config.discount_product_id;

        for (const line of lines) {
            if (product === undefined || line.get_product() !== product) {
                if (discPolicy === "replace") {
                    line.set_discount(pc);
                } else {
                    line.set_discount(line.get_discount() + pc);
                }
            }
        }
    },
});
