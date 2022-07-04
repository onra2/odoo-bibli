# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import models, fields, api


class Rent(models.Model):
    _name = 'esilecturerent.rent'
    _description = 'esilecturerent.rent'

    book_id = fields.Many2one('lecture.livre', string="Livre")
    member_id = fields.Many2one('res.partner', string="Emprunteur")
    state = fields.Selection(
        [('exemplaireprete', 'Exemplaire prete'),
         ('exemplaireretourne', 'Exemplaire retourne'),
         ('exemplaireperdu', 'Exemplaire perdu')
         ], default='exemplaireprete')
    rent_date = fields.Date(string="Date d'emprunt", default=datetime.today())
    return_date = fields.Date(string='Date de retour')

    _sql_constraints = [
        ('obligatoirBookId', 'CHECK(book_id IS NOT NULL)', 'book id ne peut etre vide'),
        ('obliMemberId', 'CHECK(member_id IS NOT NULL)', 'member_id ne peut etre vide'),
    ]

    def set_to_retourne(self):
        self.state = 'exemplaireretourne'

    def set_to_prete(self):
        self.state = 'exemplaireprete'

    def set_to_perdu(self):
        self.state = 'exemplaireperdu'

    # @api.constrains('state')
    # def _checkstate(self):
    #     for record in self:
    #         if record.state ....:
    #             raise models.ValidationError("Un livre ne peut etre emprunté avant d'etre retourné.")
