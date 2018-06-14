from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from Api.routes import make_routes
from Api.session import initialize_session


def main(global_config, **settings):
    config = Configurator(settings=settings)
    initialize_session(config)
    make_routes(config)
    return config.make_wsgi_app()
