# -*- coding: utf-8 -*-
# from odoo import http


# class RenstraFt(http.Controller):
#     @http.route('/renstra_ft/renstra_ft', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/renstra_ft/renstra_ft/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('renstra_ft.listing', {
#             'root': '/renstra_ft/renstra_ft',
#             'objects': http.request.env['renstra_ft.renstra_ft'].search([]),
#         })

#     @http.route('/renstra_ft/renstra_ft/objects/<model("renstra_ft.renstra_ft"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('renstra_ft.object', {
#             'object': obj
#         })
