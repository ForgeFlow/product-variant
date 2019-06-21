# Copyright 2019 Eficent Business and IT Consulting Services, S.L.
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class ProductVariantManualCreate(models.TransientModel):
    _name = "product.variant.manual.create"

    def _default_product_tmpl(self):
        product_tmpl_id = self.env['product.template'].browse(
            self.env.context.get('active_id'))
        if not product_tmpl_id:
            raise ValidationError(
                _("Product template not found"))
        return product_tmpl_id

    product_tmpl_id = fields.Many2one(
        string='Product Template',
        comodel_name='product.template',
        default=lambda self: self._default_product_tmpl(),
    )
    item_ids = fields.One2many(
        comodel_name='product.variant.manual.create.item',
        inverse_name='wiz_id',
        string='Wizard Items',
    )

    def create_product_variants(self):
        for item in self.item_ids:
            item.product_tmpl_id = self.product_tmpl_id
            item.create_variant_if_needed()


class ProductVariantManualCreateItem(models.TransientModel):
    _inherit = ["product.configurator"]
    _name = "product.variant.manual.create.item"

    wiz_id = fields.Many2one(
        string='Wizard',
        commodel_name='product.variant.manual.create',
        required=True, ondelete='cascade',
        readonly=True,
    )
