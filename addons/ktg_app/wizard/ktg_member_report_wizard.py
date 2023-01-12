from odoo import api, fields, models


class KtgMemberReportWizard(models.Model):
    _name = 'ktg.member.report.wizard'
    _description = 'KTG Member Report Wizard'

    member_id = fields.Many2one('ktg.member', string='Member', required=True, ondelete='cascade',
                                domain=lambda self: self._get_default_members())

    def _get_default_members(self):
        return_members = self.env['ktg.member'].search([])
        member_ids = []
        for member in return_members:
            if member.id not in member_ids:
                member_ids.append(member.id)
        return [('id', 'in', member_ids)]

    def print_report(self):
        data = {'members': self.env['ktg.member'].search_read([])}
        return self.env.ref(
            'ktg_app.action_member_report') \
            .report_action(self, data=data)
