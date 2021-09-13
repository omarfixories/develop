# -*- coding: utf-8 -*-
# from odoo import http


# class FixoMisionEspacial(http.Controller):
#     @http.route('/fixo_mision_espacial/fixo_mision_espacial/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fixo_mision_espacial/fixo_mision_espacial/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fixo_mision_espacial.listing', {
#             'root': '/fixo_mision_espacial/fixo_mision_espacial',
#             'objects': http.request.env['fixo_mision_espacial.fixo_mision_espacial'].search([]),
#         })

#     @http.route('/fixo_mision_espacial/fixo_mision_espacial/objects/<model("fixo_mision_espacial.fixo_mision_espacial"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fixo_mision_espacial.object', {
#             'object': obj
#         })
