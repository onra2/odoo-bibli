# -*- coding: utf-8 -*-
# from odoo import http


# class Lecture(http.Controller):
#     @http.route('/lecture/lecture/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lecture/lecture/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('lecture.listing', {
#             'root': '/lecture/lecture',
#             'objects': http.request.env['lecture.lecture'].search([]),
#         })

#     @http.route('/lecture/lecture/objects/<model("lecture.lecture"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lecture.object', {
#             'object': obj
#         })
