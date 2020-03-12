from odoo import api, fields, models, _

class ResUsers(models.Model):
    _inherit = 'res.users'
  
    helpdesk_code = fields.Char(
        string='Helpdesk Code')
  
    ticket_ids = fields.Many2many(
        string='Tickets',
        comodel_name='helpdesk.ticket',
        relation='helpdesk_ticket_res_users_rel',
        column1='user_id',
        column2='helpdesk_id')
 
