from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ErrorMessage(models.Model):
    _name = "report.2pdf.move_template"
    _description = "Report"

    @api.model
    def _get_report_values(self, docids, data=None):
        bad_docs = self.env['stock.picking'].search([('state', '!=', 'done')])
        nice_docs = []
        docs = self.env['stock.picking'].search([])
        for i in docs:
            for x in docids:
                if str(i) == 'stock.picking({},)'.format(str(x).replace('[', '').replace(']', '')):
                    nice_docs.append(i)

        for i in docids:
            if 'stock.picking({},)'.format(i) in str(list(bad_docs)):
                raise ValidationError('Одно или несколько выбранных перемещений не проведены')
            else:
                return {
                    'docs': nice_docs
                }
