# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class fixo_mision_espacial(models.Model):
#     _name = 'fixo_mision_espacial.fixo_mision_espacial'
#     _description = 'fixo_mision_espacial.fixo_mision_espacial'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
