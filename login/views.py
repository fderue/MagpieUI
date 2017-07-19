from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPOk, HTTPBadRequest,HTTPTemporaryRedirect
from pyramid.response import Response
import requests

external_provider = ['openid',
                     'dkrz',
                     'ipsl',
                     'badc',
                     'pcmdi',
                     'smhi']


@view_config(route_name='login', renderer='templates/login/login.mako')
def login_view(request):
    session = requests.get('http://localhost:8000/session', cookies=request.cookies)
    if session.status_code == 200:
        json_data = session.json()
        if json_data['authenticated']:
            user_name = json_data['user_name']
            return {'user_name':  user_name,
                    'external_provider': external_provider}
        else:
            if 'submit' in request.POST:
                new_location = 'http://localhost:8000/signin'
                return HTTPTemporaryRedirect(location=new_location)

    else:
        return session

    return {'external_provider': external_provider}
