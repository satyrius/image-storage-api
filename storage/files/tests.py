from django.test import TestCase


class UploadTest(TestCase):
    urls = 'files.urls'

    def test_upload(self):
        with open(__file__, 'r') as f:
            res = self.client.post('/upload', data={'file': f})
            self.assertEqual(res.status_code, 200)
            self.assertEqual(res['content-type'], 'application/json')
