# -*- coding: utf-8 -*-

from odoo import models, fields, api


class fixo_libro(models.Model):
    _name = 'fixo_biblioteca_admin.libro'
    _description = 'Modelo de libro de la biblioteca.'

    titulo = fields.Char(string='Titulo', required=True)
    paginas = fields.Integer(string='Cantidad de paginas', required=True)
    Autor = fields.Text(string='Autor')
    notas = fields.Text(string='Notas')
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
