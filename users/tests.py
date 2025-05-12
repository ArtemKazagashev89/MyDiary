from django.test import TestCase
from django.urls import reverse

from .models import CustomUser


class UserRegistrationTests(TestCase):
    def setUp(self):
        self.url = reverse("users:register")

    def test_registration_valid_data(self):
        response = self.client.post(
            self.url,
            {
                "email": "test@example.com",
                "password1": "testpassword",
                "password2": "testpassword",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(CustomUser.objects.filter(email="test@example.com").exists())

    def test_registration_invalid_data(self):
        response = self.client.post(
            self.url,
            {
                "email": "",
                "password1": "testpassword",
                "password2": "testpassword",
            },
        )
        self.assertEqual(response.status_code, 200)
        form = response.context["form"]
        self.assertFormError(form, "email", "This field is required.")


class UserLoginTests(TestCase):
    def setUp(self):
        self.url = reverse("users:login")
        self.user = CustomUser.objects.create(
            email="test@example.com",
        )
        self.user.set_password("testpassword")
        self.user.save()

    def test_login_valid_user(self):
        response = self.client.post(self.url, {"username": "test@example.com", "password": "testpassword"})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.wsgi_request.user.is_authenticated)
