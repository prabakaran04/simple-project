# copyright 2024 Prabakaran
# license OPL-1 (see license file for full copyright and licensing details).

from odoo import models, fields, api
from odoo.exceptions import ValidationError
# odoo already has a event.event model so using event.management
class EventManagement(models.Model):
    _name = 'event.management'
    _description = 'Event Management'

    name = fields.Char(string='Event Name', required=True)
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    location = fields.Char(string='Location')
    seats = fields.Integer(string='Seats')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done')
    ], string='State', default='draft')

    # commenting the below code because i have achieved it using default parameter in the field
    # @api.model
    # def create(self, vals):
    #     vals['state'] = 'draft'  # Ensure the state is set to 'draft' upon creation
    #     record = super(EventManagement, self).create(vals)  # Call the parent method
    #     return record


    def action_confirm(self):
        self.state = 'confirmed'

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for record in self:
            if record.end_date and record.start_date and record.end_date < record.start_date:
                raise ValidationError('End date must be greater than or equal to start date.')
