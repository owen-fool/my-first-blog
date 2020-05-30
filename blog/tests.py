from django.test import LiveServerTestCase

class CVPageTest(LiveServerTestCase):

    def test_uses_CV_template(self):
        response = self.client.get('/CV/')
        self.assertTemplateUsed(response, 'blog/CV.html', 'blog/base.html')
