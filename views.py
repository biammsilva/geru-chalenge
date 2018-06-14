from pyramid.response import Response
from pyramid.request import Request
from quotes.classes import Quotes

def get_quotes_view(request):
    """ View to get all the quotes from the python lib """
    define_session(request)
    return Response(json=request.session['quote_result'].get_quotes())

def get_quote_view(request):
    """ View to get one of the the quotes from the python lib """
    try:
        define_session(request)
        quote_number = int(request.matchdict['quote_number'])
        return Response(json=request.session['quote_result'].get_quote(quote_number))
    except IndexError as e:
        return Response(str(e), status_code=500)

def get_random_quote_view(request):
    """ View to get a random quote from the python lib """
    try:
        define_session(request)
        return Response(json=request.session['quote_result'].get_random_quote())
    except Exception as e:
        print(e)
        return Response(e, status_code=500)

def home_view(request):
    """ View to show the home page """
    define_session(request)
    return Response("Web Challenge 1.0")

def define_session(request):
    print(request)
    if 'quote_result' not in request.session:
        request.session['quote_result'] = Quotes()
