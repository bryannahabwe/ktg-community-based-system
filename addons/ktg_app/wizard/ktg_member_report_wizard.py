from odoo import api, fields, models


class KtgMemberReportWizard(models.TransientModel):
    _name = 'ktg.member.report.wizard'
    _description = 'KTG Member Report Wizard'

    member = fields.Many2one('ktg.member', string='Member', required=True)

    def print_report(self):
        member = self.env['ktg.member'].search([('id', '=', self.member.id)])
        drives = self.get_member_drives(member)
        subscriptions = self.get_annual_subscription(member)
        identification = {'id': member.id, 'name': member.name, 'ktg_number': member.ktg_number}
        data = {
            'identification': identification,
            'drives': drives,
            'subscriptions': subscriptions
        }
        return self.env.ref(
            'ktg_app.action_member_report') \
            .report_action(self, data=data)

    def get_member_drives(self, member):
        new_list = []
        member_result_info = self.env['ktg.drive_participation'].search([('beneficiary', '=', member.id)])
        for result in member_result_info:
            res = {
                'drive': result.drive.name,
                'amount': result.amount
            }
            new_list.append(res)
        return new_list

    def get_annual_subscription(self, member):
        new_list = []
        member_result_info = self.env['ktg.annual_subscription'].search([('beneficiary', '=', member.id)])
        for result in member_result_info:
            res = {
                'year': result.financial_year.year,
                'subscription': result.subscription
            }
            new_list.append(res)
        return new_list
