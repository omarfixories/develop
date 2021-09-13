# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class fixo_biblioteca_admin(models.Model):
#     _name = 'fixo_biblioteca_admin.fixo_biblioteca_admin'
#     _description = 'fixo_biblioteca_admin.fixo_biblioteca_admin'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
