import base64
import hashlib
import uuid

from django.db import models
from django.core.validators import URLValidator


class Url(models.Model):
    url = models.CharField(max_length=255, validators=[URLValidator()])
    url_hash = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.url

    def generate_hash(self):
        unique_id = uuid.uuid4()
        unique_hash = hashlib.sha1(str(unique_id).encode("utf8"))
        result = base64.b64encode(unique_hash.digest()).decode("utf8")

        return result[:6]

    def save(self, *args, **kwargs):
        self.url_hash = self.generate_hash()

        super(Url, self).save(*args, **kwargs)

    @classmethod
    def get_full_url(cls, url_hash=None):
        url = cls.objects.get(url_hash=url_hash)

        return url.url
