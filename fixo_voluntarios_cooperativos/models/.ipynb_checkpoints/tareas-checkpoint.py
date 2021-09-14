# -*- coding: utf-8 -*-

from odoo import models, fields, api


class fixo_tareas(models.Model):
    _name = 'fixo_voluntarios_cooperativos.tareas'
    _description = 'Modelo de tareas'

    name = fields.Char(string="Nombre de la tarea", required=True)
    horaInicio = fields.Datetime(string="Fecha de inicio", default=lambda self: fields.Datetime.now())
    horaFIn = fields.Datetime(string="Fecha de finalización", default=lambda self: fields.Datetime.now() + 5)
    periorica = fields.Boolean(string="Tarea periodica")
    periodicidad = fields.Float(string="Perioridicidad en minutos")
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
