# -*- coding: utf-8 -*-
# from odoo import http


# class ThecnicalModule(http.Controller):
#     @http.route('/thecnical_module/thecnical_module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/thecnical_module/thecnical_module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('thecnical_module.listing', {
#             'root': '/thecnical_module/thecnical_module',
#             'objects': http.request.env['thecnical_module.thecnical_module'].search([]),
#         })

#     @http.route('/thecnical_module/thecnical_module/objects/<model("thecnical_module.thecnical_module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('thecnical_module.object', {
#             'object': obj
#         })

