/*
Copyright 2023 Manuel Regidor <manuel.regidor@sygel.es>
License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
*/

import {Component} from "@odoo/owl";
import {OrderWidget} from "@point_of_sale/app/generic_components/order_widget/order_widget";
import {usePos} from "@point_of_sale/app/store/pos_hook";

export class ItemCounter extends Component {
    static template = "ItemCounter";
    setup() {
        this.pos = usePos();
    }
    get_item_count() {
        var count = 0;
        var lines = this.pos
            .get_order()
            .get_orderlines()
            .filter((line) => line.get_product().type !== "service");
        if (lines) {
            lines.forEach(function (line) {
                if (line.get_unit().is_units) {
                    count += line.qty;
                } else {
                    count += 1;
                }
            });
        }
        return count;
    }
}

OrderWidget.components = {
    ...OrderWidget.components,
    ItemCounter,
};
