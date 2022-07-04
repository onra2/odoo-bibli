from odoo import api, fields, models, exceptions
from datetime import datetime

import logging

_logger = logging.getLogger(__name__)

# La classe LectureLivre cree un livre
class LectureLivre(models.Model):
    _name = 'lecture.livre'
    nom = fields.Char('Titre')
    description = fields.Html('Description')
    image = fields.Binary('Couverture')
    date_publication = fields.Date('Date de la publication')
    nb_pages = fields.Integer('Nombre de pages')
    auteurs = fields.Many2many('res.partner', string='Auteurs')

    like_ids = fields.Many2many('res.users', relation="like_book", ondelete='cascade')
    count_likes = fields.Integer('Likes', compute='_compute_count_likes')

    #count_rent = fields.Integer('Rent count', compute='_compute_rent')

    _sql_constraints = [
        ('nameUnique', 'unique(nom)', 'nom existe deja'),
        ('nbPage_sup0', "CHECK ( (nb_pages > 0))", "Le nombre de pages doit être strictement supérieur à 0.")
    ]

    @api.depends('like_ids')
    def _compute_count_likes(self):
        for r in self:
            r.count_likes = len(r.like_ids)

    # @api.depends('res.partner.rent_ids')
    # def _compute_rent(self):
    #     member = self.env['res.partner']
    #     for r in self:
    #         r.count_rent = len(member.rent_ids)

    @api.constrains('date_publication')
    def _check_release_date(self):
        for record in self:
            if record.date_publication and record.date_publication > fields.Date.today():
                raise models.ValidationError("La date doit etre inferieur a aujourdhui.")

    def name_get(self):
        res = []
        for rec in self:
            res.append((rec.id, "%s" % rec.nom))
        return res

    def userAlreadyLiked(self):
        uid = self._uid
        user = self.env['res.users'].browse(uid)
        like = False
        for value in self.like_ids:
            if value.id == user.id:
                like = True
        return like

    def addLike(self):
        uid = self._uid
        user = self.env['res.users'].browse(uid)

        if self.userAlreadyLiked():
            self.like_ids = [(3, user.id)]
        else:
            self.write({'like_ids': [4, user.id]})