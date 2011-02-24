from pyramid.config import Configurator
from pyramid_beaker import session_factory_from_settings
from sqlalchemy import engine_from_config

from beauth.models import initialize_sql

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    config = Configurator(settings=settings)
    config.scan('beauth.models') # Import models
    session_factory = session_factory_from_settings(settings)
    config.set_session_factory(session_factory)
    config.add_static_view('static', 'beauth:static')
    config.add_route('root', '/', view='beauth.views.root',
                     view_renderer='root.mako')
    config.add_route('debug', '/debug', view='beauth.views.debug',
                     view_renderer='debug.mako')
    config.add_route('list_users', '/list', view='beauth.views.list',
                     view_renderer='list.mako')
    config.add_route('login', '/login', view='beauth.views.login',
                     view_renderer='login.mako')
    config.add_route('logout', '/logout', view='beauth.views.logout')
    config.add_route('register', '/register', view='beauth.views.register',
                     view_renderer='register.mako')
    config.add_route('view_user', '/{username}', view='beauth.views.view',
                     view_renderer='view.mako')
    initialize_sql(engine)
    return config.make_wsgi_app()


