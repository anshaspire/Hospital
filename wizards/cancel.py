
from odoo import api, fields, models, _
from datetime import date
from odoo.exceptions import ValidationError
from dateutil import relativedelta
class CancelWizard(models.TransientModel):
    _name = "cancel.wizard"
    _description = "Cancel this wizard"

    appointment_id = fields.Many2one('hospital.appointment',string="Appointment", 
    domain=['|',('state','=','draft'),('state','=','in_consulation')]
    )
    
    reason = fields.Text(string="Reason")
    
    def cancellation(self):
        cancel_day = self.env['ir.config_parameter'].get_param('hospital_mangement.cancel_day')
        print(cancel_day)
        allowed = self.appointment_id.appointment_time - relativedelta.relativedelta(days=int(cancel_day))
        print(allowed)
        if allowed <= date.today():
            raise ValidationError(_("Cancellation is not allowed"))
        else:   
            self.appointment_id.state = "cancel"
        return{
            'type' : 'ir.actions.client',
            'tag' : 'reload',
        }
