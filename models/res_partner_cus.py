from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    tipo_cliente_id = fields.Many2one('tipo.cliente', string='Tipo de Cliente')