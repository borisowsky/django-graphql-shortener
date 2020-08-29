from ariadne import MutationType

from core.models import Url

mutation = MutationType()


@mutation.field("createUrl")
def resolve_mutation_create_url(*_, **args):
    url = args.get("url")

    created_url_object = Url.objects.create(url=url)

    return {
        "id": created_url_object.id,
        "url": created_url_object.url,
        "hash": created_url_object.url_hash,
    }
