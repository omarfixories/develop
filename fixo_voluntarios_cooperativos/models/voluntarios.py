# -*- coding: utf-8 -*-

from odoo import models, fields, api


class fixo_voluntarios(models.Model):
    _name = 'fixo_voluntarios_cooperativos.voluntarios'
    _description = 'Modelo de voluntarios que cooperan'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
