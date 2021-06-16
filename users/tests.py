from mixer.backend.django import mixer

from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class TestUserModelViewSet(APITestCase):

    def test_get_users_list_unauthorized(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_users_list(self):
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin12345')

        self.client.login(username='admin', password='admin12345')
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user_detail_unauthorized(self):
        user = mixer.blend(User)

        response = self.client.get(f'/api/users/{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_user_detail(self):
        user = mixer.blend(User)
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin12345')

        self.client.login(username='admin', password='admin12345')
        response = self.client.get(f'/api/users/{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_user(self):
        user = mixer.blend(User)
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin12345')

        self.client.login(username='admin', password='admin12345')
        response = self.client.patch(f'/api/users/{user.id}/', {'first_name': 'user_test', 'age': 30})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        user = User.objects.get(id=user.id)
        self.assertEqual(user.first_name, 'user_test')
        self.assertEqual(user.age, 30)

    def test_post_user(self):
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin12345')

        self.client.login(username='admin', password='admin12345')

        response = self.client.post(f'/api/users/', {'username': 'User_1', 'password': 'qwe123+$'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_user(self):
        user = mixer.blend(User)
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin12345')

        self.client.login(username='admin', password='admin12345')

        response = self.client.delete(f'/api/users/{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
