odoo.define('dynamic_tooltip', function(require) {

    var core = require('web.core');

    var DynamicTooltip = core.list_widget_registry.get('field').extend({
        _format: function (row_data, options) {
            var value = row_data[this.id].value;
            var tip = row_data['tooltip_helper'].value;
            return value + ' <i class="fa fa-info-circle" data-toggle="tooltip" title="'+ tip +'" />';
        }
    });

    core.list_widget_registry.add('field.dynamic_tooltip', DynamicTooltip);
})
