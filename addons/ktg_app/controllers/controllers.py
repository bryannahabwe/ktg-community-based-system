# -*- coding: utf-8 -*-
# from odoo import http


# class KtgApp(http.Controller):
#     @http.route('/ktg_app/ktg_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ktg_app/ktg_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ktg_app.listing', {
#             'root': '/ktg_app/ktg_app',
#             'objects': http.request.env['ktg_app.ktg_app'].search([]),
#         })

#     @http.route('/ktg_app/ktg_app/objects/<model("ktg_app.ktg_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ktg_app.object', {
#             'object': obj
#         })
