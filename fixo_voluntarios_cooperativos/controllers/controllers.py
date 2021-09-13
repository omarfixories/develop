# -*- coding: utf-8 -*-
# from odoo import http


# class FixoVoluntariosCooperativos(http.Controller):
#     @http.route('/fixo_voluntarios_cooperativos/fixo_voluntarios_cooperativos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fixo_voluntarios_cooperativos/fixo_voluntarios_cooperativos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fixo_voluntarios_cooperativos.listing', {
#             'root': '/fixo_voluntarios_cooperativos/fixo_voluntarios_cooperativos',
#             'objects': http.request.env['fixo_voluntarios_cooperativos.fixo_voluntarios_cooperativos'].search([]),
#         })

#     @http.route('/fixo_voluntarios_cooperativos/fixo_voluntarios_cooperativos/objects/<model("fixo_voluntarios_cooperativos.fixo_voluntarios_cooperativos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fixo_voluntarios_cooperativos.object', {
#             'object': obj
#         })
