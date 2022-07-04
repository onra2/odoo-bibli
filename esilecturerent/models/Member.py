# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Member(models.Model):
    _inherit = ['res.partner']
    _name = 'res.partner'

    number = fields.Char(string="le matricule du membre")
    rent_ids = fields.Many2many('esilecturerent.rent', string='Rent ids')


