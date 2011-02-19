import unittest
from pyramid import testing

from beauth.tests import _initTestingDB

class ViewUserTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        _initTestingDB()

    def tearDown(self):
        testing.tearDown()
        
    def test_it(self):
        from beauth.views import view
        request = testing.DummyRequest()
        request.matchdict['username'] = u'admin'
        response = view(request)
        self.assertEqual(response['user'].name, u'admin')
