# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import api, fields, models, _


class HelpdeskTicket(models.Model):
    _name = 'helpdesk.ticket'
    _description = 'Ticket'

    _inherit = ['mail.thread.cc', 'mail.activity.mixin']

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

    tickets_qty = fields.Integer(
        string='Tickets Qty',
        compute='_compute_tickets_qty')

    @api.depends('responsable_id')
    def _compute_tickets_qty(self):
        ticket_obj = self.env['helpdesk.ticket']
        # import wdb; wbd.set_trace()
        # import pdb
        # pdb.set_trace()
        # (A o B) o C
        # o (o (A, B), C)
        for ticket in self:
            tickets = ticket_obj.search(
                [('responsable_id', '=', ticket.responsable_id.id)])
            ticket.tickets_qty = len(tickets)

    def set_responsable(self):
        self.ensure_one()
        # Para muchos campos mejor esta
        self.responsable_id = self.env.user.id

        # self.write({
        #    'responsable_id': self.env.user.id
        # })

    @api.onchange('name', 'date_deadline')
    def _onchange_description(self):
        if self.name and self.date_deadline:
            self.description = '%s - %s' % (self.name, self.date_deadline)
