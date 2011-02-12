from pyramid.httpexceptions import HTTPFound
from pyramid.url import route_url

from beauth.forms.user import RegistrationForm

def root(request):
    return {'project':'BEAuth'}


def register(request):
    form = RegistrationForm(request.POST)
    if request.method == 'POST' and form.validate():
        return HTTPFound(location = route_url('root', request))
    return {'form':form, 'project':'BEAuth'}
