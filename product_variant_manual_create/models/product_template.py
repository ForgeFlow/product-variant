# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3

from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    can_manually_create = fields.Boolean(
        string="Can manually create Variants",
        compute='_compute_can_manually_create',
        default=False,
    )

    def _compute_can_manually_create(self):
        for record in self:
            if (len(record.attribute_line_ids) > 0 and (
                    record.no_create_variants == 'yes' or (
                    record.no_create_variants == 'empty' and
                    record.categ_id.no_create_variants))):
                record.can_manually_create = True

    @api.multi
    def unlink(self):
        for record in self:
            self.env['product.configurator.attribute'].search([
                ('product_tmpl_id', '=', record.id)]).unlink()
        return super(ProductTemplate, self).unlink()
