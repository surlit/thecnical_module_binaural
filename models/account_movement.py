from odoo.exceptions import UserError
from odoo import _
from odoo import models, fields,api
import logging
_logger = logging.getLogger(__name__)

class AccountMove(models.Model):
    _inherit = 'account.move'

    
    # @api.onchange('invoice_line_ids')
    # def _invoice_line_ids_onchange(self):

    #     _logger.info('\n\n\n\n ')
    #     _logger.info('invoice_line_ids')
        
    #     for s in self:

    #         # if not s.partner_id:
    #         #     raise UserError(_("Por favor, seleccione un cliente antes de continuar."))
            
    #         _logger.info(s)
    #         _logger.info(s.partner_id)
    #         _logger.info(s.partner_id.tipo_cliente_id)
            