"""Paginate library"""

def list_users_url_generator(**kw):
    from pyramid.threadlocal import get_current_request
    from webhelpers.util import update_params
    new_url = update_params(get_current_request().route_url('list_users'), page=kw['page'])
    return new_url
