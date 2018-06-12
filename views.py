from pyramid.response import Response
from pyramid.request import Request
from pyramid.view import view_config

from quotes.classes import Quotes

@view_config(renderer='json')
def get_quotes_view(request):
    define_session(request)
    return Response(json=request.session['quote_result'].get_quotes(), \
                    content_type="application/json")

def get_quote_view(request):
    try:
        define_session(request)
        quote_number = int(request.matchdict['quote_number'])
        if type(quote_number) != int:
            raise ValueError("Quote number must be a integer")
        return Response(json=request.session['quote_result'].get_quote(quote_number))
    except Exception as e:
        print(e)
        return Response(e, status_code=500)

def get_random_quote_view(request):
    try:
        print("RANDOM")
        define_session(request)
        return Response(json=request.session['quote_result'].get_random_quote())
    except Exception as e:
        print(e)
        return Response(e, status_code=500)

def home_view(request):
    define_session(request)
    return Response("Web Challenge 1.0")

def define_session(request):
    if "quote_result" not in request.session:
        session = request.session
        session['quote_result'] = Quotes()
