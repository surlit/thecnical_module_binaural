from odoo.tests import TransactionCase
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)
class TestResPartner(TransactionCase):

    def setUp(self):
        super().setUp()
        # Crear un partner de prueba
        self.partner = self.env['res.partner'].create({
            'name': 'PRUEBA_1',
        })
        
        _logger.info('Se a creado un usuario res_partner')

    def test_minorista_sin_rif(self):
        """Un minorista debe poder guardarse sin RIF"""
        minorista = self.env.ref('thecnical_module_binaural.tipo_minorista')

        self.partner.write({
            'tipo_cliente_id': minorista,
            'vat': False,
        })
        _logger.info('Se a actulizado a tipo de cliente minorista')

        self.assertEqual(self.partner.tipo_cliente_id, minorista)
        _logger.info('Se verifica que no valide al ser minorista')

        self.assertFalse(self.partner.vat)

    def test_mayorista_sin_rif_falla(self):
        """Un mayorista sin RIF debe lanzar ValidationError"""
        mayorista = self.env.ref('thecnical_module_binaural.tipo_mayorista')
        
        with self.assertRaises(ValidationError):
            self.partner.write({
                'tipo_cliente_id': mayorista,
                'vat': False,
            })
        _logger.info('Se actualiza mayorista  sin rif y se valida correctamente')

    def test_mayorista_con_rif_ok(self):
        """Un Mayorista con RIF debe guardarse correctamente"""
        self.partner.write({
            'tipo_cliente_id': 'Mayorista',
            'vat': 'V-12345678-9',
        })
        self.assertEqual(self.partner.vat, 'V-12345678-9')
        _logger.info('Se actualiza mayorista con rif y se guarda adecuadamente')

    
