from django.test import TestCase, Client
from django.urls import reverse
from shorter.views import index, link_redir
from shorter.models import Link


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index_url = reverse('shorter:index')
        self.link_redir_url = reverse('shorter:link_redir', args=['testCase'])
        Link.objects.create(
            url='https://www.jetbrains.com/',
            code='testCase'
        )

    def test_index_GET(self):
        response = self.client.get(self.index_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'shorter/index.html')

    def test_link_redir_GET(self):
        response = self.client.get(self.link_redir_url)

        self.assertEquals(response.status_code, 302)
