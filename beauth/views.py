from pyramid.httpexceptions import HTTPFound
from pyramid.url import current_route_url

from webhelpers import paginate

from beauth.lib.paginate import list_users_url_generator
from beauth.forms.user import RegistrationForm
from beauth.models import DBSession
from beauth.models import User

def root(request):
    return {'project':'BEAuth'}

def view(request):
    username = request.matchdict['username']
    user = User.by_name(name=username)
    return {'user':user, 'project':'BEAuth'}

def register(request):
    user = User(name=None, password=None, email=None)
    form = RegistrationForm(request.POST)
    if request.method == 'POST' and form.validate():
        user.name = form.name.data
        user.password = form.password.data
        user.email = form.email.data
        DBSession.add(user)
        return HTTPFound(location = route_url('view_user', request, username=user.name))
    return {'form':form, 'project':'BEAuth'}

def list(request):
    try:
        page_number = request.GET['page']
    except:
        page_number = '1'

    try:
        query = request.GET['query']
    except:
        query = ''

    users = DBSession.query(User)

    currentPage = paginate.Page(users, page=page_number, items_per_page=10, url=list_users_url_generator)
    return {'currentPage':currentPage, 'users':currentPage.items}
