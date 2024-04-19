odoo.define("pos_receipt_employee_name.models", function (require) {
  "use strict";

  const models = require("point_of_sale.models");
  models.load_fields('hr.employee','pos_receipt_name');

  var _super_order = models.Order.prototype;
  models.Order = models.Order.extend({
      export_for_printing() {
          const receipt = _super_order.export_for_printing.apply(this, arguments);
          if (this.employee && this.employee.pos_receipt_name){
            receipt['cashier'] = this.employee.pos_receipt_name;
          }
          return receipt;
      },
  });
})
