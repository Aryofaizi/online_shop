from django.test import TestCase
from django.contrib.auth import get_user_model


class Test(TestCase):
    def test_signup_view(self):
        user = get_user_model().objects.create_user(
            username="test",
            password="test",
            email="test",
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, user.username)
