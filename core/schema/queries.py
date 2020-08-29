from ariadne import QueryType

from core.models import Url

query = QueryType()


@query.field("hello")
def resolve_query_hello(*_):
    return "Hello world!"


@query.field("url")
def resolve_query_url(*_, **args):
    url_hash = args.get('hash')
    url_object = Url.objects.get(url_hash=url_hash)

    return {
        "id": url_object.id,
        "url": url_object.url,
        "hash": url_object.url_hash,
    }
