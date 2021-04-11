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
        # self.test_account_create()

    def tearDown(self):
        pass

    def test_user_list(self):
        request = self.factory.get('/users')
        force_authenticate(request, user=self.user)
        response = UserController.list(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_account_create(self):
        payload = {
            'name': 'testingUser',
            'email': 'test@email.com',
            'created_at': '2019-09-30'
        }
        request = self.factory.post('/users', payload)
        force_authenticate(request, user=self.user)
        response = UserController.create(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # def test_account_create_invalid(self):
    #     view = AccountController.as_view({'post': 'create'})
    #     payload = {
    #         'name': 'testingUser',
    #         'email': 'test@email.com'
    #     }
    #     request = self.factory.post('/api/accounts/', payload)
    #     response = view(request)

    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # def test_account_details(self):
    #     view = AccountController.as_view({'get': 'account_detail'})
    #     request = self.factory.get('/api/accounts/1')
    #     response = view(request, pk=1)

    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_account_details_not_found(self):
    #     view = AccountController.as_view({'get': 'account_detail'})
    #     request = self.factory.get('/api/accounts/2')
    #     response = view(request, pk=2)

    #     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # def test_account_update(self):
    #     view = AccountController.as_view({'put': 'update'})
    #     payload = {
    #         'name': 'testingUpdateUser',
    #         'email': 'test@email.com',
    #         'created_at': '2018-09-30'
    #     }
    #     request = self.factory.put('/api/accounts/1', payload)
    #     response = view(request, pk=1)

    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_account_update_invalid(self):
    #     view = AccountController.as_view({'put': 'update'})
    #     payload = {
    #         'name': 'testingUpdateUser',
    #         'email': 'test@email.com'
    #     }
    #     request = self.factory.put('/api/accounts/1', payload)
    #     response = view(request, pk=1)

    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # def test_account_delete(self):
    #     view = AccountController.as_view({'put': 'delete'})
    #     request = self.factory.delete('/api/accounts/1')
    #     response = view(request, pk=1)

    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # def test_account_delete_invalid(self):
    #     view = AccountController.as_view({'put': 'delete'})
    #     request = self.factory.delete('/api/accounts/2')
    #     response = view(request, pk=2)

    #     self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
