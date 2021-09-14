# -*- coding: utf-8 -*-

from odoo import models, fields, api


class fixo_nave(models.Model):
    _name = 'fixo_mision_espacial.nave'
    _description = 'Nave de la mision espacial'

    nombre = fields.Char(string='Nombre de la nave', required=True)
    pasajeros = fields.Integer(string='Cantidad de pasajeros',default=15)
    descripcion = fields.Text(string='Descripción de la nave')
    active = fields.Boolean(string='Activo')
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
