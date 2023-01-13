from odoo import models, fields, api


class KtgAnnualSubscription(models.Model):
    _name = "ktg.annual_subscription"
    _description = "Annual Subscription"
    _rec_name = "beneficiary"

    beneficiary = fields.Many2one('ktg.member', 'Member', required=True, )
    ktg_number = fields.Char('KTG Number', help="KTG Member Number", readonly="1")
    subscription = fields.Monetary('Subscription', required=True, readonly=True, default=20000)
    financial_year = fields.Many2one('ktg.financial_year', 'Financial Year', required=True)
    date_created = fields.Datetime('Date Created', readonly=True, default=fields.Datetime.now)
    date_of_payment = fields.Date('Date of Payment',)
    currency_id = fields.Many2one('res.currency', string='Currency',
                                  default=lambda self: self.env.user.company_id.currency_id)

    @api.onchange('beneficiary')
    def onchange_beneficiary(self):
        if self.beneficiary:
            self.ktg_number = self.beneficiary.ktg_number
