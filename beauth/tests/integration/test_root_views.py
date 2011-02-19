import unittest
from pyramid import testing

from beauth.tests import _initTestingDB

class ViewRootTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()
        
    def test_it(self):
        from beauth.views import root
        request = testing.DummyRequest()
        response = root(request)
        self.assertEqual(response['project'], u'BEAuth') 
