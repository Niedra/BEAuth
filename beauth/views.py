from pyramid.httpexceptions import HTTPFound
from pyramid.url import route_url

from beauth.forms.user import RegistrationForm
from beauth.models import DBSession
from beauth.models import User

def root(request):
    return {'project':'BEAuth'}

def register(request):
    user = User(name=None, password=None, email=None)
    form = RegistrationForm(request.POST)
    if request.method == 'POST' and form.validate():
        user.name = form.name.data
        user.password = form.password.data
        user.email = form.email.data
        DBSession.add(user)
        return HTTPFound(location = route_url('root', request))
    return {'form':form, 'project':'BEAuth', 'request':request.POST}
