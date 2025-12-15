from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    mode_tipo_cliente = fields.Boolean(string="Modo tipo cliente", config_parameter="thecnical_binaural.modo_tipo_cliente")
    descuento_mayorista = fields.Float(string="Descuento para Mayoristas (%)", config_parameter='thecnical_binaural.descuento_mayorista')
    exigir_rif_mayorista = fields.Boolean(string="Exigir RIF a Mayoristas", config_parameter='thecnical_binaural.exigir_rif_mayorista')
    descuento_distribuidor = fields.Float(string="Descuento para Distribuidores (%)", config_parameter='thecnical_binaural.descuento_distribuidor')
    exigir_rif_distribuidor = fields.Boolean(string="Exigir RIF a Distribuidores", config_parameter='thecnical_binaural.exigir_rif_distribuidor')
    descuento_vip = fields.Float(string="Descuento para vips (%)", config_parameter='thecnical_binaural.descuento_vip')
    exigir_rif_vip = fields.Boolean(string="Exigir RIF a vips", config_parameter='thecnical_binaural.exigir_rif_vip')