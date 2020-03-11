from django.test import TestCase

from shorter.models import Link


class TestModels(TestCase):

    def setUp(self):
        self.Link1 = Link.objects.create(
            url='https://www.jetbrains.com/',
        )

    def test_link_is_code_assigned_on_creation(self):
        self.assertTrue(self.Link1.code)

    def test_link_is_qr_assigned_on_creation(self):
        self.assertTrue(self.Link1.qr)

    def test_link_code_is_unique(self):
        with self.assertRaises(Exception) as context:
            Link_uni1 = Link.objects.create(
                url='https://www.jetbrains.com/',
                code='testCase'
            )
            Link_uni2 = Link.objects.create(
                url='https://www.jetbrains.com/',
                code='testCase'
            )
        self.assertTrue('UNIQUE' in str(context.exception))
