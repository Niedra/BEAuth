from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from beauth.models import initialize_sql

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_sql(engine)
    config = Configurator(settings=settings)
    config.add_static_view('static', 'beauth:static')
    config.add_route('root', '/', view='beauth.views.root',
                     view_renderer='root.mako')
    config.add_route('list_users', '/list', view='beauth.views.list',
                     view_renderer='list.mako')
    config.add_route('register', '/register', view='beauth.views.register',
                     view_renderer='register.mako')
    config.add_route('view_user', '/{username}', view='beauth.views.view',
                     view_renderer='view.mako')
    return config.make_wsgi_app()


