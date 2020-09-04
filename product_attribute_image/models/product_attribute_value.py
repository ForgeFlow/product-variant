# Copyright 2020 ForgeFlow S.L.(http://www.forgeflow.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models


class ProductAttributeValue(models.Model):
    _name = "product.attribute.value"
    _inherit = ["product.attribute.value", "image.mixin"]
