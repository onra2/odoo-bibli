from odoo import api, fields, models, exceptions

# La classe Author etend res_partner, elle cree un auteur
class Author(models.Model):
    _inherit = 'res.partner'
    _order = 'name'
    authored_book_ids = fields.Many2many('lecture.livre', string='Authored Books')
    count_books = fields.Integer('Number of Authored Books', compute='_compute_count_books', store=True)

    author = fields.Boolean('isAuthor', default=False)

    @api.depends('authored_book_ids')
    def _compute_count_books(self):
        for r in self:
            r.count_books = len(r.authored_book_ids)
