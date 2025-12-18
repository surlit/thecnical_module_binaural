from odoo.exceptions import UserError
from odoo import models, fields,api,_
import logging
_logger = logging.getLogger(__name__)

class AccountMove(models.Model):
    _inherit = 'account.move.line'

    
    @api.onchange('product_id')
    def _product_onchange(self):

        ICPSUDO = self.env['ir.config_parameter'].sudo()
        
        mode_cliente = ICPSUDO.get_param('thecnical_binaural.modo_tipo_cliente')
        
        for s in self:

            if not s.partner_id:
                raise UserError(_("Por favor, seleccione un cliente antes de continuar."))
            
            if mode_cliente and s.partner_id.tipo_cliente_id and s.partner_id.tipo_cliente_id.descuento:
                
                self.discount = s.partner_id.tipo_cliente_id.descuento 
                
                
            
            
            