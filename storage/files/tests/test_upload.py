import json
from os import path
from django.test import TestCase


class UploadTest(TestCase):
    urls = 'files.urls'

    def setUp(self):
        self.filename = path.join(path.dirname(__file__), 'my_dog.jpg')

    def upload(self, file, expected_code=200):
        res = self.client.post('/upload', data={'file': file})
        self.assertEqual(res.status_code, expected_code)
        self.assertEqual(res['content-type'], 'application/json')
        return json.loads(res.content)

    def test_upload(self):
        with open(self.filename, 'r') as f:
            data = self.upload(f)
            self.assertNotIn('errors', data)

    def test_upload_not_an_image(self):
        with open(__file__, 'r') as f:
            data = self.upload(f, 400)
            self.assertIn('errors', data)
            self.assertIsInstance(data['errors'], dict)
            self.assertIn('file', data['errors'])
