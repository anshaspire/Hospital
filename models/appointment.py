from odoo import api, fields, models, _
from datetime import date
from odoo.exceptions import ValidationError

 
class HospitalAppointment(models.Model):
    _name = "hospital.appointment"

    _description = "Hospital Appointment"
    
    
    patient_id = fields.Many2one('hospital.patient',string="Patient")
    gender  = fields.Selection(related='patient_id.gender')
    age = fields.Integer(related='patient_id.age') 
    appointment_time = fields.Date(string="Appointment time")
    booking_date = fields.Date(string="Booking Date",default=fields.Date.context_today)
    ref = fields.Char(string='Reference')
    prescription = fields.Html(string="Prescription")
    state = fields.Selection([
        ('draft','Draft'),
        ('in_consulation','In Consulation'),
        ('done','Done'),
        ('cancel','Cancelled')],string="Status", default='draft',required= True                                                 
        ) 
    priority = fields.Selection(
        string='priority',
        selection=[('0', ''), 
        ('1', 'Low'),
        ('2','High'),
        ('3','Very High')]
    )
    doctor_id = fields.Many2one('res.users',string="Doctor")
    pharmacy_id = fields.One2many('hospital.pharmacy','appointment_id',string="Pharmacy")
    hide_sales = fields.Boolean(string="Hide Sales")
    @api.constrains('appointment_time')
    def check_apd(self):
        for rec in self:
            if rec.appointment_time and rec.appointment_time < fields.Date.today():
                raise ValidationError(_("The appointment date is invalid"))

    @api.onchange('patient_id')
    def _onchange_patient_id(self):
        self.ref = self.patient_id.ref

    def action_test(self):
        return{
            'type':'ir.actions.act_url',
            'target':'new',
            'url' : 'https://www.google.com',
        }

    def action_in_consultation(self):
        for rec in self:
            rec.state = "in_consulation"
    def action_done(self):
        for rec in self:
            rec.state = "done"
    def action_cancel(self):
        for rec in self:
            rec.state = "cancel"
    def action_draft(self):
        for rec in self:
            rec.state = "draft"

class HospitalPharmacy(models.Model):
    _name = "hospital.pharmacy"
    _description = "Appointment Pharmacy Lines"

    product_id = fields.Many2one('product.product',required=True)
    price = fields.Float(string="Price")
    qty  = fields.Integer(string="Quantity")
    appointment_id = fields.Many2one('hospital.appointment',string="Appointment")
