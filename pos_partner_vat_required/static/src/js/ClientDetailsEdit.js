/*
Copyright 2023 Manuel Regidor <manuel.regidor@sygel.es>
License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
*/

odoo.define('pos_partner_vat_required.ClientDetailsEdit', function(require) {

    const ClientDetailsEdit = require('point_of_sale.ClientDetailsEdit');
    const Registries = require('point_of_sale.Registries');
    const session = require('web.session');
    var core = require('web.core');

    var _t = core._t;

    VatRequiredClientDetailsEdit = ClientDetailsEdit => class extends ClientDetailsEdit {
        saveChanges() {
            if (!this.changes.vat){
                return this.showPopup('ErrorPopup', {
                  title: _t('VAT Is Required'),
                });
            }
            super.saveChanges();
        }
    };

    Registries.Component.extend(ClientDetailsEdit, VatRequiredClientDetailsEdit);

    return ClientDetailsEdit;
});
