from odoo import models, fields, api,_
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)
class ResPartner(models.Model):
    _inherit = 'res.partner'

    tipo_cliente_id = fields.Many2one('tipo.cliente', string='Tipo de Cliente')

    @api.constrains('tipo_cliente_id')
    def _onchange_tipo_cliente_id(self):
        minorista = self.env.ref('thecnical_module_binaural.tipo_minorista')
        _logger.info('minorista')
        _logger.info(minorista)
        for s in self:
            _logger.info('s.tipo_cliente_id')
            _logger.info(s.tipo_cliente_id)
            if s.tipo_cliente_id.exigir_rif and s.tipo_cliente_id.name  and s.tipo_cliente_id != minorista and not s.vat:
                raise ValidationError("Por favor agregar un rif para poder disfrutar del decuento")