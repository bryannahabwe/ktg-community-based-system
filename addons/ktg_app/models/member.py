from odoo import models, fields, api, _


class KtgMember(models.Model):
    _name = "ktg.member"
    _description = "display_name"

    name = fields.Char('Member Name', required=True)
    display_name = fields.Char('Display Name', compute='_compute_display_name')
    phone_number = fields.Char('Telephone Number')
    ktg_number = fields.Char('KTG Number', help="KTG Member Number", readonly="1", index=True)
    date_created = fields.Datetime('Date Created', readonly=True, default=fields.Datetime.now)

    @api.model
    def create(self, vals):
        vals['ktg_number'] = self.env['ir.sequence'].next_by_code('ktg.member.number')
        return super(KtgMember, self).create(vals)

    @api.depends('name', 'ktg_number')
    def _compute_display_name(self):
        for record in self:
            name = '%s' % (record.name or '')
            ktg_number = '%s' % (record.ktg_number or '')
            record.display_name = _("%s ( %s )") % (name, ktg_number)

    def name_get(self):
        result = []
        for drive in self:
            name = drive.display_name
            result.append((drive.id, name))
        return result
