from pyramid.httpexceptions import HTTPFound
from pyramid.url import route_url

from webhelpers import paginate

from beauth.lib.paginate import list_users_url_generator
from beauth.forms.user import RegistrationForm
from beauth.forms.user import LoginForm
from beauth.models import DBSession
from beauth.models import User

def root(request):
    return {'project':'BEAuth'}

def view(request):
    username = request.matchdict['username']
    user = User.by_name(name=username)
    return {'user':user, 'project':'BEAuth'}

def login(request):
    form = LoginForm(request.POST)
    session = request.session
    if request.method == 'POST' and form.validate():
        user = User.by_name(name=form.name.data)

        if user and user.check_password(form.password.data):
            usersession = {'name': user.name}
            session["user"] = usersession
            session.save()
            return HTTPFound(location = route_url('root', request))

    return {'form':form, 'project':'BEAuth'}

def logout(request):
    session = request.session
    session["user"] = None
    session.delete()
    return HTTPFound(location = route_url('root', request))

def register(request):
    user = User(name=None, password='', email=None)
    form = RegistrationForm(request.POST)
    if request.method == 'POST' and form.validate():
        user.name = form.name.data
        user.password = form.password.data
        user.email = form.email.data
        DBSession.add(user)
        return HTTPFound(location = route_url('view_user', request, username=user.name))
    return {'form':form, 'project':'BEAuth'}

def list(request):
    page_number = request.GET.get('page', '1')
    query = request.GET.get('query', '')

    users = DBSession.query(User)

    currentPage = paginate.Page(users, page=page_number, items_per_page=10, url=list_users_url_generator)
    return {'currentPage':currentPage, 'users':currentPage.items}

def debug(request):
    session = request.session
    return {'session':session, 'project':'BEAuth'}
