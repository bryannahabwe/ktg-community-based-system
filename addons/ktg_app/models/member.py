from odoo import models, fields


class KtgMember(models.Model):
    _name = "ktg.member"
    _description = "Member"

    name = fields.Char('Member Name')
    phone_number = fields.Char('Telephone Number')
    ktg_number = fields.Char('KTG Number')
