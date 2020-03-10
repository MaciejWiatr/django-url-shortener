from django.test import SimpleTestCase
from django.urls import reverse, resolve
from shorter.views import index, link_redir


class TestUrls(SimpleTestCase):

    def test_index_url_is_resovlved(self):
        url = reverse('shorter:index')
        self.assertEquals(resolve(url).func, index)

    def test_link_redir_url_is_resovlved(self):
        url = reverse('shorter:link_redir', args=['testCode'])
        self.assertEquals(resolve(url).func, link_redir)
