from odoo.exceptions import AccessError, UserError
from odoo.tests.common import TransactionCase
import logging
from datetime import datetime
from psycopg2 import IntegrityError
from odoo.tools import mute_logger

_logger = logging.getLogger(__name__)


class TestLecture(TransactionCase):

    def test_create_date_constraint(self):
        "Create a Livre avec date > aujourhdui"
        Livre = self.env['lecture.livre']
        with self.assertRaises(Exception) as context:
            Livre.create({'nom': 'Coucou',
                          'date_publication': '2022-12-08',
                          'nb_pages': '200'
                          })
            self.assertTrue('La date doit etre inferieur a aujourdhui.' == context.exception[0])

    def test_create_pages_count_exception(self):
        "Create a book with 0 pages"
        Livre = self.env['lecture.livre']
        with self.assertRaises(IntegrityError):
            with mute_logger('odoo.sql_db'):
                Livre.create({'nom': 'Coucou',
                              'date_publication': '2022-12-08',
                              'nb_pages': '0'
                              })

    def test_duplicate_name(self):
        "Two livres with same name"
        Livre = self.env['lecture.livre']
        with self.assertRaises(Exception):
            with mute_logger('odoo.sql_db'):
                Livre.create({'nom': 'Coucou',
                              'date_publication': '2024-12-08',
                              'nb_pages': '5'
                              })
                Livre.create({'nom': 'Coucou',
                              'date_publication': '2026-12-08',
                              'nb_pages': '5'
                              })