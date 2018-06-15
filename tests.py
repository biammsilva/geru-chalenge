import unittest

from pyramid import testing
from webtest import TestApp
from Api import main
from quotes.classes import Quotes

class TestCase(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        app = main({})
        self.testapp = TestApp(app)

    def tearDown(self):
        testing.tearDown()

    def test_home(self):
        res = self.testapp.get('/', status=200)
        self.assertIn(b'Web Challenge 1.0', res.body)

    def test_get_all_quotes_is_up(self):
        res = self.testapp.get('/quotes')
        self.assertIn("200 OK", res.status)

    def test_get_random_quote_is_up(self):
        res = self.testapp.get('/quotes/random')
        self.assertIn("200 OK", res.status)

    def test_get_quote_is_up(self):
        res = self.testapp.get('/quotes/1')
        self.assertIn("200 OK", res.status)

    def test_quotes_data(self):
        res = self.testapp.get('/quotes')
        self.assertEqual(Quotes().get_quotes(), res.json)

    def test_quote_id_data(self):
        number = 2
        res = self.testapp.get('/quotes/'+str(number))
        self.assertEqual(Quotes().get_quote(number), res.json)

    def test_quote_wrong_id(self):
        with self.assertRaises(IndexError):
            Quotes().get_quote(20)
