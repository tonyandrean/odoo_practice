from odoo import http
from odoo.http import request
import json
import logging
from .limit import rate_limit
from .api_check import check_api_key

_logger = logging.getLogger(__name__)


class VendorController(http.Controller):

    @http.route('/api/vendor', type='json', auth='public', methods=['post'], csrf=False)
    def create_vendor(self, **kwargs):
        check_api_key()
        rate_limit()
        try:
            if not kwargs.get('name'):
                return {
                    'status': 'error',
                    'message': 'Vendor name is required.'
                }

            vendor = request.env['res.partner'].sudo().create({
                'name': kwargs.get('name'),
                'supplier_rank': 1,
                'email': kwargs.get('email'),
                'phone': kwargs.get('phone'),
                'mobile': kwargs.get('mobile'),
                'street': kwargs.get('street'),
                'street2': kwargs.get('street2'),
                'city': kwargs.get('city'),
                'state_id': kwargs.get('state_id'),
                'zip': kwargs.get('zip'),
                'country_id': kwargs.get('country_id'),
                'website': kwargs.get('website'),
                'vat': kwargs.get('vat'),
                'company_type': kwargs.get('company_type', 'company')
            })
            return {
                'status': 'success',
                'id': vendor.id,
                "message": f"Success created {vendor.name}."
            }

        except Exception as e:
            return {
                'jsonrpc': '2.0',
                'id': None,
                'error': {
                    'code': 500,
                    'message': 'Internal Server Error',
                    'data': str(e)
                }
            }

    @http.route('/api/vendor/<int:vendor_id>', type='json', auth='public', methods=['get'], csrf=False)
    def read_vendor(self, vendor_id):
        check_api_key()
        rate_limit()
        try:
            vendor = request.env['res.partner'].sudo().browse(vendor_id)
            if not vendor.exists() or vendor.is_company == False:
                return json.dumps({
                    'status': 'error',
                    'message': 'Vendor not found'
                })

            data = {
                'id': vendor.id,
                'name': vendor.name if vendor.name else '',
                'email': vendor.email if vendor.email else '',
                'phone': vendor.phone if vendor.phone else '',
                'mobile': vendor.mobile if vendor.mobile else '',
                'street': vendor.street if vendor.street else '',
                'street2': vendor.street2 if vendor.street2 else '',
                'city': vendor.city if vendor.city else '',
                'state_id': {
                    'id': vendor.state_id.id,
                    'name': vendor.state_id.name
                } if vendor.state_id else {'id': '', 'name': ''},
                'zip': vendor.zip if vendor.zip else '',
                'country_id': {
                    'id': vendor.country_id.id,
                    'name': vendor.country_id.name
                } if vendor.country_id else {'id': '', 'name': ''},
                'website': vendor.website if vendor.website else '',
                'vat': vendor.vat if vendor.vat else '',
                'comment': vendor.comment if vendor.comment else '',
                'company_type': vendor.company_type,
                'is_company': vendor.is_company,
                'active': vendor.active
            }
            return json.dumps({
                'status': 'success',
                'data': data
            })

        except Exception as e:
            return json.dumps({
                'status': 'error',
                'message': str(e)
            })

    @http.route('/api/vendor/<int:vendor_id>', type='json', auth='public', methods=['put'], csrf=False)
    def update_vendor(self, vendor_id, **kwargs):
        check_api_key()
        try:
            vendor = request.env['res.partner'].sudo().browse(vendor_id)
            if not vendor.exists() or vendor.is_company == False:
                return {
                    'status': 'error',
                    'message': 'Vendor not found'
                }

            update_values = {}
            allowed_fields = [
                'name', 'email', 'phone', 'mobile', 'street', 'street2',
                'city', 'state_id', 'zip', 'country_id', 'website',
                'vat', 'comment', 'company_type', 'active'
            ]

            for field in allowed_fields:
                if field in kwargs:
                    update_values[field] = kwargs[field]
            vendor.write(update_values)

            return {
                'status': 'success',
                "message": f"Vendor {vendor.name} updated successfully."
            }

        except Exception as e:
            return {
                'status': 'error',
                'message': str(e)
            }

    @http.route('/api/vendor/<int:vendor_id>', type='json', auth='public', methods=['delete'], csrf=False)
    def delete_vendor(self, vendor_id):
        check_api_key()
        try:
            vendor = request.env['res.partner'].sudo().browse(vendor_id)
            if not vendor.exists() or vendor.is_company == False:
                return {
                    'status': 'error',
                    'message': 'Vendor not found'
                }

            vendor_name = vendor.name
            vendor.unlink()
            return {
                'status': 'success',
                "message": f"Vendor {vendor_name} deleted successfully."
            }

        except Exception as e:
            return {
                'status': 'error',
                'message': str(e)
            }