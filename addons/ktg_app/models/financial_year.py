from odoo import models, fields


class KtgFinancialYear(models.Model):
    _name = "ktg.financial_year"
    _description = "Financial Year"
    _rec_name = "year"

    year = fields.Char('Financial Year', required=True)
