from odoo import models, fields, api




class ProjectWizard(models.TransientModel):
    _name = 'project.wizard'
    _description = 'Create Project from Space Mission'



    name = fields.Char(string="Name")
    label = fields.Char(string="Name of the Tasks")
    partner_id = fields.Many2one('res.partner', string="Customer")
    mission_id = fields.Many2one('mission.model', string="Mission")
    tag_ids = fields.Many2many('project.tags', string="Tags")
    user_id = fields.Many2one('res.users', string="Project Manager")
    date_start = fields.Date(string="Date Start")
    date_end = fields.Date(string="Date End")


    def create_project(self):
        for rec in self:
            project_data = {
                'name': rec.name,
                'label_tasks': rec.label,
                'partner_id': rec.partner_id.id,
                'mission_id': rec.mission_id.id,
                'tag_ids': [(6, 0, rec.tag_ids.ids)],
                'user_id': rec.user_id.id,
                'date_start': rec.date_start,
                'date': rec.date_end
            }
            self.env['project.project'].create(project_data)

        return {'type': 'ir.actions.client',
                'tag': 'reload'}