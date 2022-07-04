from odoo import api, fields, models

# La classe product_livre etend product_template, elle ajoute un attribut collection a product template
class product_livre(models.Model):
    _inherit = "product.template"

    collection = fields.Many2many('lecture.livre', string="Composés des livres")
