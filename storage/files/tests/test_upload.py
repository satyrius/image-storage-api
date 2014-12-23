from os import path
from django.test import TestCase


class UploadTest(TestCase):
    urls = 'files.urls'

    def setUp(self):
        self.filename = path.join(path.dirname(__file__), 'my_dog.jpg')

    def test_upload(self):
        with open(self.filename, 'r') as f:
            res = self.client.post('/upload', data={'file': f})
            self.assertEqual(res.status_code, 200)
            self.assertEqual(res['content-type'], 'application/json')
