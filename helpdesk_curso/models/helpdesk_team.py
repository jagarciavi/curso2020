# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import api, fields, models, _

class HelpdeskTeam(models.Model):
    _name = 'helpdesk.team'
    _description = 'Helpdesk Team'

    name = fields.Char(string='Name', required=True)
    ticket_ids = fields.One2many(string='Tickets', comodel_name='helpdesk.ticket', inverse_name='team_id')
    