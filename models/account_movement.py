from odoo.exceptions import UserError
from odoo import _
from odoo import models, fields,api
import logging
_logger = logging.getLogger(__name__)

class AccountMove(models.Model):
    _inherit = 'account.move'
    
    tipo_cliente_id = fields.Many2one(
            'tipo.cliente',
            related='partner_id.tipo_cliente_id',
            string='Tipo de Cliente',
            readonly=True,
            store=False  # o True si necesitas usarlo en búsquedas/filtros
        )