# -*- coding: utf-8 -*-
# from odoo import http


# class FixoBibliotecaAdmin(http.Controller):
#     @http.route('/fixo_biblioteca_admin/fixo_biblioteca_admin/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fixo_biblioteca_admin/fixo_biblioteca_admin/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fixo_biblioteca_admin.listing', {
#             'root': '/fixo_biblioteca_admin/fixo_biblioteca_admin',
#             'objects': http.request.env['fixo_biblioteca_admin.fixo_biblioteca_admin'].search([]),
#         })

#     @http.route('/fixo_biblioteca_admin/fixo_biblioteca_admin/objects/<model("fixo_biblioteca_admin.fixo_biblioteca_admin"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fixo_biblioteca_admin.object', {
#             'object': obj
#         })
