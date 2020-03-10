from django.test import SimpleTestCase
from shorter.forms import LinkForm


class TestForms(SimpleTestCase):

    def test_link_form_valid_data(self):
        form = LinkForm(data={
            'url': 'https://www.jetbrains.com/'
        })

        self.assertTrue(form.is_valid())

    def test_link_form_no_data(self):
        form = LinkForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_link_form_wrong_data(self):
        form = LinkForm(data={
            'url': 'TotallyNotALink'
        })

        self.assertFalse(form.is_valid())
