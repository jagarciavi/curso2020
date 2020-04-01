from odoo import models, api, fields, _

class HelpDeskTicket(models.Model):
    
    _inherit = 'helpdesk.ticket'

    project_id = fields.Many2one(
        string='Project',
        comodel_name='project.project')
    
    task_id = fields.Many2one(
        string='Task',
        comodel_name='project.task')

    @api.onchange('task_id')
    def _onchange_task_id(self):
        if self.task_id and self.task_id.project_id:
            self.project_id = self.task_id.project_id
        else:
            self.project_id = False
    
    
    @api.onchange('project_id')
    def _onchange_project_id(self):
        if self.project_id:
            domain={'task_id': [('project_id','=',self.project_id.id)]}
        else:
            domain = {}
        
        return {'domain': domain}
    