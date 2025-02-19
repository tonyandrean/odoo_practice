from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def update_standard_price_from_vendor(self):
        selected_categories = self.env['product.category'].search([('name', 'in', ['Office Furniture'])])
        products = self.search([('categ_id', 'in', selected_categories.ids)])

        for product in products:
            vendor_price = product.seller_ids and product.seller_ids[0].price or 0.0
            vendor_currency = product.seller_ids and product.seller_ids[0].currency_id or False

            if vendor_price and vendor_currency and vendor_currency != product.currency_id:
                new_standard_price = vendor_currency._convert(vendor_price, product.currency_id,
                                                              product.env.company, fields.Date.today())
                product.write({'standard_price': new_standard_price})
                _logger.info(f"Updated {product.name}: {new_standard_price} {product.currency_id.name}")