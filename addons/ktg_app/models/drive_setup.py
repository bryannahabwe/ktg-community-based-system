from odoo import models, fields, api


class KtgDriveSetup(models.Model):
    _name = "ktg.drive_setup"
    _description = "Drive Set Up"

    name = fields.Char('Drive Name', required=True)
    beneficiary = fields.Many2one('ktg.member', 'Member', required=True, )
    ktg_number = fields.Char('KTG Number', help="KTG Member Number", readonly="1")
    financial_year = fields.Many2one('ktg.financial_year', 'Financial Year', required=True)
    start_time = fields.Datetime('Start', required=True, default=fields.Datetime.now)
    end_time = fields.Datetime('End', required=True, default=fields.Datetime.now)
    date_created = fields.Datetime('Date Created', readonly=True, default=fields.Datetime.now)

    @api.onchange('beneficiary')
    def onchange_beneficiary(self):
        if self.beneficiary:
            self.ktg_number = self.beneficiary.ktg_number
