from rest_framework import status
from rest_framework.test import (
    APIRequestFactory,
    APITestCase,
    force_authenticate)

from src.app.models import User
from src.app.controllers import user as UserController


class UserIntegrationTest(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create(name='test', email='test@test.com', password='test1234')

    def tearDown(self):
        pass

    def test_user_list(self):
        request = self.factory.get('/users')
        force_authenticate(request, user=self.user)
        response = UserController.list(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_account_create(self):
        payload = {
            'username': 'testingUser',
            'email': 'test@email.com',
            'password': 'test1234'
        }
        request = self.factory.post('/users', payload)
        force_authenticate(request, user=self.user)
        response = UserController.create(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_account_create_invalid(self):
        payload = {
            'email': 'test@email.com',
            'password': ''
        }
        request = self.factory.post('/users', payload)
        force_authenticate(request, user=self.user)
        response = UserController.create(request)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_details(self):
        request = self.factory.get('/users/1')
        force_authenticate(request, user=self.user)
        response = UserController.get(request, id=1)

        self.assertEqual(response.data, self.user)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_details_invalid(self):
        request = self.factory.get('/users/1')
        force_authenticate(request, user=self.user)
        response = UserController.get(request, id=1)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_account_details_not_found(self):
        request = self.factory.get('/users/3')
        force_authenticate(request, user=self.user)
        response = UserController.get(request, id=3)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_account_update(self):
        payload = {
            'username': 'updatedUser',
            'email': 'updated@email.com',
            'password': 'updatedPassword'
        }
        request = self.factory.put('/users', payload)
        force_authenticate(request, user=self.user)
        response = UserController.update(request, id=1)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_account_update_invalid(self):
        payload = {
            'username': '',
            'email': ''
        }
        request = self.factory.put('/users', payload)
        force_authenticate(request, user=self.user)
        response = UserController.update(request, id=1)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_account_delete(self):
        request = self.factory.delete('/users')
        force_authenticate(request, user=self.user)
        response = UserController.delete(request, id=1)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_account_delete_invalid(self):
        request = self.factory.delete('/users')
        force_authenticate(request, user=self.user)
        response = UserController.delete(request, id=3)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
