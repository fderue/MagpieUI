
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory



def main(global_settings, **settings):
    session_factory = SignedCookieSessionFactory(settings['auth.secret'])

    config = Configurator(
        settings=settings,
        session_factory=session_factory
    )
    config.include('pyramid_mako')
    config.include('login')
    config.include('home')
    config.include('management')

    config.scan()
    return config.make_wsgi_app()


if __name__ == '__main__':
    settings = {
        'auth.secret': 'seekrit',
        'magpie.url': 'http://localhost:8000'
    }
    app = main({}, **settings)
    from wsgiref.simple_server import make_server

    server = make_server('0.0.0.0', 5003, app)
    server.serve_forever()
