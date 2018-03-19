from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient

from api.models.restaurant import Restaurant


class RestaurantTestCase(TestCase):
    """
    Test class to test Restaurant model
    """

    def setUp(self):
        self.restaurant_name = "restaurant name"
        self.restaurant = Restaurant(name=self.restaurant_name)

    def test_create_restaurant(self):
        """
        Test restaurant creation
        """
        self.restaurant.save()
        self.assertIsNotNone(Restaurant.objects.filter(name=self.restaurant_name).first())


class RestaurantAPITestCase(APITestCase):
    """
    Test class to test Restaurant API
    """

    def setUp(self):
        self.apiClient = APIClient()
        self.restaurant_name = "restaurant name"
        self.restaurant_json = {'name': self.restaurant_name}

    def test_api_create_restaurant(self):
        """
        Test restaurant creation using API
        """
        response = self.client.post(reverse('restaurant'), self.restaurant_json, format="json")
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_api_get_restaurants(self):
        """
        Test restaurant retrieval using API
        """
        response = self.client.get(reverse('restaurant'))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
