from odoo.exceptions import UserError
from odoo import _
from odoo import models, fields,api
import logging
_logger = logging.getLogger(__name__)

class AccountMove(models.Model):
    _inherit = 'account.move'
    
    @api.onchange('invoice_line_ids')
    def _invoice_line_ids_onchange(self):

        _logger.info('\n\n\n\n ')
        _logger.info('invoice_line_ids en account move')
        
        _logger.info(self.amount_total)
        _logger.info(self.amount_untaxed)
        _logger.info(self.amount_untaxed)        
        
        
        for s in self:
            
            _logger.info(s)
            
            