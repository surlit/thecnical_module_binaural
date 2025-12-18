from odoo import models, fields, api,_
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)
class ResPartner(models.Model):
    _inherit = 'res.partner'

    tipo_cliente_id = fields.Many2one('tipo.cliente', string='Tipo de Cliente')

    @api.constrains('tipo_cliente_id')
    def _onchange_tipo_cliente_id(self):
        
        for s in self:
            
            if s.tipo_cliente_id.exigir_rif and s.tipo_cliente_id.name  and s.tipo_cliente_id.name != 'Minorista' and not s.vat:
                raise UserError(_("Por favor agregar un rif para poder disfrutar del decuento"))