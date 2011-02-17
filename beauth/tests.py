import unittest
from pyramid.config import Configurator
from pyramid import testing

def _initTestingDB():
    from sqlalchemy import create_engine
    from beauth.models import initialize_sql
    session = initialize_sql(create_engine('sqlite://'))
    return session

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
