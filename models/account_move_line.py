from odoo.exceptions import UserError
from odoo import _
from odoo import models, fields,api
import logging
_logger = logging.getLogger(__name__)

class AccountMove(models.Model):
    _inherit = 'account.move.line'

    
    @api.onchange('product_id')
    def _product_onchange(self):

        _logger.info('\n\n\n\n ')
        _logger.info('account.move.line')
        
        ICPSUDO = self.env['ir.config_parameter'].sudo()
        
        mayorista = ICPSUDO.get_param('thecnical_binaural.descuento_mayorista')
        distribuidor = ICPSUDO.get_param('thecnical_binaural.descuento_distribuidor')
        vip = ICPSUDO.get_param('thecnical_binaural.descuento_vip')
        if mayorista:
            mayorista = float(mayorista)
        if distribuidor:
            distribuidor = float(distribuidor)
        if vip:
            vip = float(vip)
        _logger.info('mayorista')
        _logger.info(mayorista)
        _logger.info('distribuidor')
        _logger.info(distribuidor)
        _logger.info('vip')
        _logger.info(vip)
        
        for s in self:

            if not s.partner_id:
                raise UserError(_("Por favor, seleccione un cliente antes de continuar."))
            
            _logger.info(s)
            # _logger.info(s.read())
            _logger.info(s.partner_id)
            if s.partner_id.tipo_cliente_id:
                _logger.info(s.partner_id.tipo_cliente_id.read())
            
            
            