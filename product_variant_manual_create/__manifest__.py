# Copyright 2019 Eficent Business and IT Consulting Services, S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Product Variant Manual Create',
    'summary': """
        Provides the functionality to manually create product variants.""",
    'version': '12.0.1.0.0',
    'category': 'Product Variant',
    'license': 'AGPL-3',
    'author': 'Eficent, '
              'Odoo Community Association (OCA)',
    'website': 'https://github.com/OCA/product-variant',
    'depends': [
        "product_variant_configurator",
    ],
    'data': [
        'wizard/product_variant_manual_create_wizard.xml',
        'views/product_template_views.xml',
    ],
}
