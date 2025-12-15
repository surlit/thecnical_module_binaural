# -*- coding: utf-8 -*-

from odoo import models, fields, api



class TipoCliente(models.Model):
    _name = 'tipo.cliente'
    _description = 'Tipos de Cliente'

    name = fields.Char('Nombre', required=True)

# En res.partner
class ResPartner(models.Model):
    _inherit = 'res.partner'

    tipo_cliente_id = fields.Many2one('tipo.cliente', string='Tipo de Cliente')