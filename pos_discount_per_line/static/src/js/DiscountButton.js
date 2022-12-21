/*
* Copyright 2022 Manuel Regidor <manuel.regidor@sygel.es>
* License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
*/

odoo.define('pos_discount_per_line.DiscountPerLineButton', function(require) {
    'use strict';

    const PosComponent = require('point_of_sale.PosComponent');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const { useListener } = require('web.custom_hooks');
    const Registries = require('point_of_sale.Registries');

    class DiscountPerLineButton extends PosComponent {
        constructor() {
            super(...arguments);
            useListener('click', this.onClick);
        }
        async onClick() {
            var self = this;
            var discountPerLineMethod = this.env.pos.config.discount_per_line == 'sum' ? 'sum' : 'replace'
            const { confirmed, payload } = await this.showPopup('NumberPopup',{
                title: this.env._t('Discount Percentage'),
                startingValue: this.env.pos.config.discount_pc,
                isInputSelected: true,
                discountPerLine: true,
                discountPerLineMethod: discountPerLineMethod,
            });            
            if (confirmed) {
                var discPolicy = document.getElementById('disc_policy').value;
                const val = Math.round(Math.max(0,Math.min(100,parseFloat(payload))));
                await self.apply_discount(val, discPolicy);
            }
        }

        async apply_discount(pc, discPolicy) {
            var order    = this.env.pos.get_order();
            var lines    = order.get_orderlines();
            var product = false;
            if (this.env.pos.config.discount_product_id){
                product = this.env.pos.config.discount_product_id[0];
            }
            for (const line of lines){
                if (product === undefined || line.get_product() != product) {
                    if (discPolicy == 'replace'){
                        line.set_discount(pc);
                    }else{
                        line.set_discount(line.get_discount() + pc);
                    }
                }               
            }
        }
    }

    DiscountPerLineButton.template = 'DiscountPerLineButton';

    ProductScreen.addControlButton({
        component: DiscountPerLineButton,
        condition: function () {
            return true;
        },
    });

    Registries.Component.add(DiscountPerLineButton);

    return DiscountPerLineButton;
});
