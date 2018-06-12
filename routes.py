from views import get_quotes_view, get_quote_view, home_view

def make_routes(config):
    config.add_route('home', '/')
    config.add_view(home_view, route_name='home')
    config.add_route('quotes', '/quotes')
    config.add_view(get_quotes_view, route_name='quotes')
    config.add_route('quote', '/quote/{quote_number}')
    config.add_view(get_quote_view, route_name='quote')
