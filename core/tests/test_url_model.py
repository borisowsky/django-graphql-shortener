from django.test import TestCase

from core.models import Url


class TestUrlModel(TestCase):
    def test_generate_hash(self):
        """Can generate short hash for URL"""

        testing_url = "http://example.com"

        url = Url.objects.create(url=testing_url)
        url_hash = url.url_hash

        self.assertIsInstance(url_hash, str)

    def test_get_full_url_by_hash(self):
        """Can get full url by hash"""

        testing_url = "http://example.com"

        url = Url.objects.create(url=testing_url)
        url_hash = url.url_hash

        url_in_db = Url.get_full_url(url_hash)

        self.assertEqual(url_in_db, testing_url)
