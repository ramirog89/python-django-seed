from rest_framework import status
from rest_framework.test import (
    APIRequestFactory,
    APITestCase,
    force_authenticate)

from src.app.models import User
from src.app.dtos.user import UserDto
from src.app.controllers import authentication as AuthenticationController


class AuthIntegrationTest(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(username='test', name='test', email='test@test.com', password='test1234')

    def tearDown(self):
        pass

    def test_login(self):
        payload = {
            'username': 'test',
            'password': 'test1234'
        }
        request = self.factory.post('/auth/login', payload)
        response = AuthenticationController.login(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_invalid(self):
        payload = {
            'username': '',
            'password': ''
        }
        request = self.factory.post('/auth/login', payload)
        response = AuthenticationController.login(request)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_logout(self):
        request = self.factory.post('/auth/logout')
        force_authenticate(request, user=self.user)
        response = AuthenticationController.logout(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
