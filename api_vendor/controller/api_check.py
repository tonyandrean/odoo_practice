from odoo.http import request
from odoo.exceptions import AccessDenied

def check_api_key():
    try:
        api_key = request.httprequest.headers.get('API-Key')
        if not api_key:
            raise AccessDenied("API Key is missing.")

        user = request.env['res.users'].sudo().search([('api_key', '=', api_key)], limit=1)
        if not user:
            raise AccessDenied("Invalid API Key.")

        request.update_context(user=user)
        request.env = request.env(user=user)

    except Exception as e:
        raise AccessDenied(f"Authentication error: {str(e)}")