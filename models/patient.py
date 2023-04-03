from datetime import date
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = [ 'mail.thread', 'mail.activity.mixin']
    _description = "Hospital Patient"
    _rec_name = 'name'

    name = fields.Char(string='Name',tracking=True)
    dateofbirth = fields.Date(string="Date Of Birth")
    ref = fields.Char(string='Reference')
    age = fields.Integer(string='Age',compute='computeage',tracking=True)
    gender  = fields.Selection([('Male','male'),('Female','female')], string='Gender')
    active = fields.Boolean(string='Active',default=True)
    appointment_id = fields.Many2one('hospital.appointment',string="Appointment")
    email_id = fields.Char(string="Email") 
    is_birthday = fields.Boolean(string="Birthday",compute='compute_birthday')
    phone = fields.Char(string="Phone")
    website = fields.Char(string="Website")
    appointment_count = fields.Integer(compute="compute_appointment_count", string="Appointment Count", store=True)

    @api.depends('dateofbirth')
    def computeage(self):
        for rec in self:
            today = date.today()
            if rec.dateofbirth:
                rec.age = today.year - rec.dateofbirth.year
            else:
                rec.age = 0
    
    @api.constrains('dateofbirth')
    def check_db(self):
        for rec in self:
            if rec.dateofbirth and rec.dateofbirth > fields.Date.today():
                raise ValidationError(_("The entered is not possible"))
    
    @api.depends('dateofbirth')
    def compute_birthday(self):
        for rec in self:
            is_birthday = False
            if rec.dateofbirth:
                today = date.today()
                if today.day == rec.dateofbirth.day and today.month == rec.dateofbirth.month:
                    is_birthday = True
                
            rec.is_birthday = is_birthday

    @api.depends('appointment_id')
    def compute_appointment_count(self):
        pass
        # appointment_group = self.env['hospital.appointment'].read_group(domain=[],fields=['patient_id'],groupby=['patient_id'])
        # for appointment in appointment_group:
        #     patient_id = appointment.get('patient_id')[0]
        #     patient_rec  = self.browse(patient_id)
        #     patient_rec.appointment_count = appointment['patient_id']
        #     self -= patient_rec
        # self.appointment_count = 0
        