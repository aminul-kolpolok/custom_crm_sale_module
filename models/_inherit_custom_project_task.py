from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import AccessError, UserError, ValidationError





class ProjectTasks(models.Model):
    _inherit = 'project.task'


    reporter = fields.Many2one('project.task', string="Task Reporter.")
    emp_comments = fields.Html(translate=True)











# class SaleOrderLine(models.Model):
#     _inherit = 'sale.order.line'
#
#     sl_no = fields.Integer(string="SI")
#     receive_datetime = fields.Datetime(string='Receive Datetime', default=lambda self: fields.datetime.now())
#     payment_types = fields.Selection(string="Payment Type", selection=PAYMENT_STATUS, default='bank_asia')




