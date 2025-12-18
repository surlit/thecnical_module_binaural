from odoo.tests import TransactionCase
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)
class TestFacturaConDescuento(TransactionCase):

    def setUp(self):
        super().setUp()
        
        self.product = self.env['product.product'].create({
            'name': 'Producto de Prueba',
            'list_price': 100.0,
        })
        
        
        self.tipo_mayorista = self.env.ref('thecnical_module_binaural.tipo_mayorista')
        
        
        self.partner = self.env['res.partner'].create({
            'name': 'Cliente Mayorista',
            'tipo_cliente_id': self.tipo_mayorista.id,
            'vat': 'V-12345678-9',  
        })
        _logger.info('Se a creado usuario Mayorista')
        
        

    def test_factura_con_descuento(self):
        """Crear una factura para un cliente Mayorista y verificar que se aplica el descuento."""
        
        
        invoice = self.env['account.move'].create({
            'move_type': 'out_invoice',  
            'partner_id': self.partner.id,
            'invoice_line_ids': [
                (0, 0, {
                    'product_id': self.product.id,
                    'quantity': 2,
                    'price_unit': self.product.list_price,
                    
                })
            ]
        })
        _logger.info('Se a creado una factura con descuento Mayorista')
        
        
        invoice.invoice_line_ids._onchange_product_id()
        
        
        
        self.assertEqual(invoice.invoice_line_ids.discount, 5.0)
        _logger.info(f'Se a verificado el descuento de {invoice.invoice_line_ids.discount}%')

    
    def test_factura_sin_descuento(self):
        """Crear una factura para un cliente Mayorista y verificar que se aplica el descuento."""
        
        self.tipo_minorista = self.env.ref('thecnical_module_binaural.tipo_minorista')
        
        self.partner_2 = self.env['res.partner'].create({
            'name': 'Cliente Minorista',
            'tipo_cliente_id': self.tipo_minorista.id,
            'vat': 'V-18345123',  
        })
        _logger.info('Se a creado usuario Minorista')

        
        invoice = self.env['account.move'].create({
            'move_type': 'out_invoice',  
            'partner_id': self.partner_2.id,
            'invoice_line_ids': [
                (0, 0, {
                    'product_id': self.product.id,
                    'quantity': 2,
                    'price_unit': self.product.list_price,
                    
                })
            ]
        })
        _logger.info('se ha creado una factura de un cliente minorista sin descuento')
        
        invoice.invoice_line_ids._onchange_product_id()
        
        
        
        self.assertEqual(invoice.invoice_line_ids.discount, 0.0)
        _logger.info('se ha verificado que no tenga descuento')
    def test_factura_sin_tipo_cliente(self):
        """Crear una factura para un cliente Mayorista y verificar que se aplica el descuento."""
        
        self.tipo_minorista = self.env.ref('thecnical_module_binaural.tipo_minorista')
        
        self.partner_2 = self.env['res.partner'].create({
            'name': 'Cliente_X',
            
            'vat': 'V-23123456',  
        })
        _logger.info('Se a creado usuario sin cliente')

        
        invoice = self.env['account.move'].create({
            'move_type': 'out_invoice',  
            'partner_id': self.partner_2.id,
            'invoice_line_ids': [
                (0, 0, {
                    'product_id': self.product.id,
                    'quantity': 2,
                    'price_unit': self.product.list_price,
                    
                })
            ]
        })
        _logger.info('se ha creado una factura de un cliente  sin tipo de cliente')
        
        invoice.invoice_line_ids._onchange_product_id()
        
        
        
        self.assertEqual(invoice.invoice_line_ids.discount, 0.0)
        _logger.info('se ha verificado que no tenga descuento ni de error')