import time

from odoo import api, fields, models


class KtgMemberReport(models.Model):
    _name = "ktg.member_report"
    _description = "KTG Member Report"

    # def get_member_results(self, member_record):
    #     new_list = []
    #     member_result_info = self.env['ktg.member'].search([('id', '=', member_record.id)])
    #     for result in member_result_info:
    #         res = {
    #             'name': result.name,
    #             'ktg_number': result.ktg_number
    #         }
    #         new_list.append(res)
    #     return new_list

    # def get_result_lines(self, result_record):
    #     lines = []
    #     for line in result_record:
    #         lines.extend(line)
    #     return lines

    @api.model
    def _get_report_values(self, docids, data=None):
        member_info = self.env['ktg.member'].browse(docids)
        print("Member Info:  ", member_info)
        docargs = {
            'doc_ids': self.ids,
            'doc_model': self.env['ktg.member'],
            'docs': member_info,
            'time': time
        }
        return docargs
