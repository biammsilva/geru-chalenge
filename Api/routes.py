from Api.views import get_quotes_view, get_quote_view, home_view, get_random_quote_view

def make_routes(config):
    config.add_route('home', '/')
    config.add_view(home_view, route_name='home')
    config.add_route('quotes', '/quotes')
    config.add_view(get_quotes_view, route_name='quotes')
    config.add_route('quote_random_number', '/quotes/random')
    config.add_view(get_random_quote_view, route_name='quote_random_number')
    config.add_route('quote_number', '/quotes/{quote_number}')
    config.add_view(get_quote_view, route_name='quote_number')
