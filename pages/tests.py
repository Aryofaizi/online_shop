from django.test import TestCase
from django.shortcuts import reverse


class Test(TestCase):

    def test_home_page_template_used(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "_base.html")
