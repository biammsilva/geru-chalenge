from pyramid.session import SignedCookieSessionFactory
from pyramid.config import Configurator

def initialize_session(config):
    my_session_factory = SignedCookieSessionFactory('itsaseekreet')
    config.set_session_factory(my_session_factory)
