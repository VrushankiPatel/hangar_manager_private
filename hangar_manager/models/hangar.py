from odoo import api, fields, models, _

class Hangar(models.Model):
    _name = "hangar.manager.hangar"
    _description = "Hangar Information"

    name = fields.Char(string="Hangar Name", required=True)
    capacity = fields.Integer(string="Capacity")
    status = fields.Selection([('available', 'Available'), ('occupied', 'Occupied')], string="Status", default="available")
    slots_available = fields.Integer(string="Slots Available")
