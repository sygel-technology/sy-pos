import {NumberPopup} from "@point_of_sale/app/utils/input_popups/number_popup";

export class NumberPopupDPL extends NumberPopup {
    static template = "pos_discount_per_line.NumberPopupDPL";
    static props = {
        ...super.props,
        discountPerLineMethod: {type: String, optional: true},
    };
}
