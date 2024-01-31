from odoo import api, fields, models, _

class HangarSlots(models.Model):
    _name = "hangar.manager.slots"
    _description = "Hangar Slots Information"

    name = fields.Char(string="Slot Name", required=True)
    price = fields.Integer(string="Price")
    

