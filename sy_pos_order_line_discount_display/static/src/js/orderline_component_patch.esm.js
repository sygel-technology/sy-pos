/* eslint-disable jsdoc/check-tag-names */
/** @odoo-module **/

import {Orderline} from "@point_of_sale/app/generic_components/orderline/orderline";
import {patch} from "@web/core/utils/patch";

patch(Orderline, {
    props: {
        ...Orderline.props,
        line: {
            ...Orderline.props.line,
            shape: {
                ...Orderline.props.line.shape,
                pricelistDiscountPercent: {type: String, optional: true},
                manualDiscountPercent: {type: String, optional: true},
                priceAfterPricelist: {type: String, optional: true},
            },
        },
    },
});
