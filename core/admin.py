from django.contrib import admin

from core.models import Url

admin.site.register(Url, readonly_fields=["url_hash"])
