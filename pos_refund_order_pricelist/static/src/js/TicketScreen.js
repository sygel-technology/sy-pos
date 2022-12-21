/*!
 *  Copyright 2022 Manuel Regidor <manuel.regidor@sygel.es>
 *  License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
 */

odoo.define('pos_refund_order_pricelist.TicketScreen', function(require) {
    'use strict';

    const TicketScreen = require('point_of_sale.TicketScreen');
    const Registries = require('point_of_sale.Registries');

    const PosDeTicketScreen = TicketScreen => class extends TicketScreen {

        async _onDoRefund() {
            await super._onDoRefund();
            const order = this.getSelectedSyncedOrder();
            if (order.pricelist){
                this.env.pos.get_order().set_pricelist(order.pricelist);
            }
            this._onCloseScreen(this.props.destinationOrder);
        }
    }
    
    Registries.Component.extend(TicketScreen, PosDeTicketScreen);
    return TicketScreen;
}
)
