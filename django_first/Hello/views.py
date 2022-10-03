from django.http import HttpResponse, HttpRequest
from .services.get_random_name import get_random_name
from webargs.djangoparser import use_args
from webargs import fields


@use_args({'name': fields.Str()}, location="query")
# noinspection PyUnusedLocal
def hello(request: HttpRequest, args) -> HttpResponse:
    if args.get('name') is None:
        name = get_random_name()
    else:
        name = args['name']
    return HttpResponse(f'Hello, {name}')
