# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import api, fields, models, _

class HelpdeskTicket(models.Model):
    _name = 'helpdesk.ticket'
    _description = 'Ticket'

    name = fields.Char(string='Name', required=True)
    description = fields.Text('Description')
    date_deadline = fields.Datetime('Date limit')
    team_id = fields.Many2one(
        string='Team',
        comodel_name='helpdesk.team')
    Stage_id = fields.Many2one(
        string='Stage',
        comodel_name='helpdesk.ticket.stage')
    user_ids = fields.Many2many(
        string='Users',
        comodel_name='res.users',
        relation='helpdesk_ticket_res_users_rel',
        column1='helpdesk_id',
        column2='user_id')
    
    responsable_id = fields.Many2one(
        string='Responsable',
        comodel_name='res.users')


    def set_responsable(self):
        self.ensure_one()
        # Para muchos campos mejor esta
        self.responsable_id = self.env.user.id

        #self.write({
        #    'responsable_id': self.env.user.id
        #})
    
