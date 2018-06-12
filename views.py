from pyramid.response import Response
from pyramid.request import Request
from pyramid.view import view_config

from quotes.classes import Quotes

@view_config(renderer='json')
def get_quotes_view(request):
    return Response(json=request.session['quote_result'].get_quotes(), \
                    content_type="application/json")

def get_quote_view(request):
    try:
        quote_number = int(request.matchdict['quote_number'])
        return Response(json=request.session['quote_result'].get_quote(quote_number))
    except Exception as e:
        print(e)
        return Response(e, status_code=500)

def home_view(request):
    session = request.session
    session['quote_result'] = Quotes()
    return Response("Web Challenge 1.0")
