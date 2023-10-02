from django.urls import reverse
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User, AnonymousUser
from chat.views import index, login_view, signin_view, logout_view, overview_view
import factory


# User factory for creating test user instances
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f"testuser{n}")
    email = factory.Faker('email')


class ChatViewsTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = UserFactory.create()
        self.user.set_password('testpassword')
        self.user.save()

    def test_index_view_authenticated(self):
        request = self.factory.get(reverse('chat'))  # Assuming 'index' is the name of the URL pattern for the index view
        request.user = self.user
        response = index(request)
        self.assertEqual(response.status_code, 200)

    def test_index_view_unauthenticated(self):
        request = self.factory.get(reverse('chat'))
        request.user = AnonymousUser()
        response = index(request)
        self.assertEqual(response.status_code, 302)  # Should redirect to login

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('login'), {
            'username': self.user.username,
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 302)  # Should redirect to chat

    def test_signin_view(self):
        response = self.client.get(reverse('signin'))
        self.assertEqual(response.status_code, 200)

    def test_logout_view(self):
        self.client.login(username=self.user.username, password='testpassword')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Should redirect to login

    def test_overview_view(self):
        self.client.login(username=self.user.username, password='testpassword')
        response = self.client.get(reverse('overview'))
        self.assertEqual(response.status_code, 200)