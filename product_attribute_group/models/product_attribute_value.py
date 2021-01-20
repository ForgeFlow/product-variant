# Copyright 2020 Akretion (https://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


from odoo import fields, models


class ProductAttributeValue(models.Model):
    _inherit = "product.attribute.value"

    group_ids = fields.Many2many(comodel_name="product.attribute.group", string="Product Attribute Groups")
