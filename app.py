from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from routes import make_routes
from session import initialize_session

if __name__ == '__main__':
    with Configurator() as config:
        initialize_session(config)
        make_routes(config)
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
