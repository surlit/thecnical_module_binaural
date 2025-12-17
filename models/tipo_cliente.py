# -*- coding: utf-8 -*-

from odoo import models, fields, api
class TipoCliente(models.Model):
    _name = 'tipo.cliente'
    _description = 'Tipos de Cliente'

    name = fields.Char('Nombre', required=True)
    descuento = fields.Char('Descuento')
    exigir_rif = fields.Boolean('Exigir Rif') 
    active  = fields.Boolean('Active')
