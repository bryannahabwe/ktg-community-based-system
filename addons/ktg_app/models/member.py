from odoo import models, fields, api


class KtgMember(models.Model):
    _name = "ktg.member"
    _description = "Member"

    name = fields.Char('Member Name', required=True)
    phone_number = fields.Char('Telephone Number')
    ktg_number = fields.Char('KTG Number', help="KTG Member Number", readonly="1", index=True)
    date_created = fields.Datetime('Date Created', readonly=True, default=fields.Datetime.now)

    @api.model
    def create(self, vals):
        vals['ktg_number'] = self.env['ir.sequence'].next_by_code('ktg.member.number')
        return super(KtgMember, self).create(vals)
