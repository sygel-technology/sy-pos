/*
Copyright 2023 Manuel Regidor <manuel.regidor@sygel.es>
License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
*/

odoo.define('pos_items_counter.ItemsCounter', function(require) {
'use strict';

    const PosComponent = require('point_of_sale.PosComponent');
    const Registries = require('point_of_sale.Registries');
    const utils = require('web.utils');

    class ItemsCounter extends PosComponent {
        get_items_count() {
            var count = 0;
            var lines = this.env.pos.get_order().get_orderlines().filter(line => line.get_product().type != 'service');
            if (lines){
                lines.forEach(function(line) {
                    console.log(line.pos.units_by_id[line.product.uom_id[0]])
                    if (line.pos.units_by_id[line.product.uom_id[0]].is_units){
                        count += line.quantity;
                    }else{
                        count += 1;
                    }                    
                });
            }
            return count;
        }
    }
    ItemsCounter.template = 'ItemsCounter';

    Registries.Component.add(ItemsCounter);

    return ItemsCounter;
});
