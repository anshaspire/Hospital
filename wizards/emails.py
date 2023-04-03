from odoo import api, fields, models

class PatientSendEmail(models.TransientModel):
    _name = "patient_send_email"
    _description = "Send Email To Patient"
    # _inherit = ['hospital.patient', 'mail.thread', 'mail.activity.mixin']
    tag_ids = fields.Many2many('ir.model.fields', string='Tags', 
    domain=[('model','=','hospital.patient')]
    )
    
    def send_mail_action(self):

        web1 = []
        for rec in self.tag_ids:
            web1.append(rec.name)
        context = {
            'url' : web1
        }
        
        template_id = self.env.ref('hospital_mangement.patient_email')
        mail_id = template_id.with_context(context).send_mail(self.env.context['active_id'],force_send = True) 
        

             
        
    
            