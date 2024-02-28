from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import AccessError, UserError, ValidationError



PAYMENT_STATUS = [
    ('bank_asia', 'Bank Asia'),
    ('upwork', 'Upwork'),
    ('paypal', 'Paypal'),
    ('mfs', 'MFS'),
    ('external', 'External')
]


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # payment_types = fields.Selection(string="Payment Type",  selection=PAYMENT_STATUS, default='bank_asia')
    # price_unit = fields.Float(readonly=False, required=False)
    service_note = fields.Text(string="Service Note.")












class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    sl_no = fields.Integer(string="SI")
    receive_datetime = fields.Datetime(string='Receive Datetime', default=lambda self: fields.datetime.now())
    payment_types = fields.Selection(string="Payment Type", selection=PAYMENT_STATUS, default='bank_asia')




