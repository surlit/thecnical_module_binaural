from odoo.tests import TransactionCase
from odoo.exceptions import ValidationError

class TestResPartner(TransactionCase):

    def setUp(self):
        super().setUp()
        # Crear un partner de prueba
        self.partner = self.env['res.partner'].create({
            'name': 'Cliente de Prueba',
        })

    def test_minorista_sin_rif(self):
        """Un minorista debe poder guardarse sin RIF"""
        self.partner.write({
            'tipo_cliente': 'minorista',
            'vat': False,
        })
        self.assertEqual(self.partner.tipo_cliente, 'minorista')
        self.assertFalse(self.partner.vat)

    def test_mayorista_sin_rif_falla(self):
        """Un mayorista sin RIF debe lanzar ValidationError"""
        with self.assertRaises(ValidationError):
            self.partner.write({
                'tipo_cliente': 'mayorista',
                'vat': False,
            })

    def test_mayorista_con_rif_ok(self):
        """Un mayorista con RIF debe guardarse correctamente"""
        self.partner.write({
            'tipo_cliente': 'mayorista',
            'vat': 'V-12345678-9',
        })
        self.assertEqual(self.partner.vat, 'V-12345678-9')