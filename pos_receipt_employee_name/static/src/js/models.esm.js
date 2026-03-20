import {PosOrder} from "@point_of_sale/app/models/pos_order";
import {patch} from "@web/core/utils/patch";

patch(PosOrder.prototype, {
    getCashierName() {
        if (this.employee_id && this.employee_id.pos_receipt_name) {
            return this.employee_id.pos_receipt_name;
        }
        return super.getCashierName();
    },
});
