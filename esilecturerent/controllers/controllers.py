# -*- coding: utf-8 -*-
# from odoo import http


# class Esilecturerent(http.Controller):
#     @http.route('/esilecturerent/esilecturerent/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/esilecturerent/esilecturerent/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('esilecturerent.listing', {
#             'root': '/esilecturerent/esilecturerent',
#             'objects': http.request.env['esilecturerent.esilecturerent'].search([]),
#         })

#     @http.route('/esilecturerent/esilecturerent/objects/<model("esilecturerent.esilecturerent"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('esilecturerent.object', {
#             'object': obj
#         })
