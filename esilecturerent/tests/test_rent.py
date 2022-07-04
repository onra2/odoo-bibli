from odoo.exceptions import AccessError, UserError
from odoo.tests.common import TransactionCase
import logging
from datetime import datetime
from psycopg2 import IntegrityError
from odoo.tools import mute_logger

_logger = logging.getLogger(__name__)


class TestLecture(TransactionCase):
    def test_emprunt_avant_retour(self):
        "emprunt livre emprunté avant le retourner"
        Livre = self.env['esilecturerent.rent']
        with self.assertRaises(IntegrityError):
            Livre.create({'book_id': 0,
                          'member_id': 0,
                          'state': 'exemplaireprete'
                          })