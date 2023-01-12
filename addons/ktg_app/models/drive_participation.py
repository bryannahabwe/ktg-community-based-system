from odoo import models, fields, api


class KtgDriveParticipation(models.Model):
    _name = "ktg.drive_participation"
    _description = "Drive Participation"
    _rec_name = "beneficiary"

    beneficiary = fields.Many2one('ktg.member', 'Member', required=True, )
    ktg_number = fields.Char('KTG Number', help="KTG Member Number", readonly="1")
    amount = fields.Monetary('Amount Contributed', required=True, )
    drive = fields.Many2one('ktg.drive_setup', 'Drive', required=True)
    date_created = fields.Datetime('Date Created', readonly=True, default=fields.Datetime.now)
    currency_id = fields.Many2one('res.currency', string='Currency',
                                  default=lambda self: self.env.user.company_id.currency_id)

    @api.onchange('beneficiary')
    def onchange_beneficiary(self):
        if self.beneficiary:
            self.ktg_number = self.beneficiary.ktg_number
