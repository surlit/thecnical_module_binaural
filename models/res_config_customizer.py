from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    mode_tipo_cliente = fields.Boolean(string="Modo tipo cliente", config_parameter="thecnical_binaural.modo_tipo_cliente")
    