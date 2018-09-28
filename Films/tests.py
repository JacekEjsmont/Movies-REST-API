from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase


class MovieTests(APITestCase):
    def test_get_movie(self):
        url = reverse('movies')
        data = {}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_movie(self):
        url = reverse('movies')
        data = {'Title': 'Rocky'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class CommentTests(APITestCase):
    def test_get_comment(self):
        url = reverse('comments')
        data = {}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
