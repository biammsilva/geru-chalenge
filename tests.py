import unittest

from pyramid import testing
from webtest import TestApp
from Api import main

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
