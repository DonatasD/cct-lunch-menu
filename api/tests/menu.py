from datetime import datetime

from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient

from api.models.menu import Menu
from api.models.restaurant import Restaurant


class MenuTestCase(TestCase):
    """
    Test class to test Menu model
    """

    def setUp(self):
        self.restaurant_name = "restaurant name"
        self.restaurant = Restaurant(name=self.restaurant_name)
        self.menu_name = "menu name"
        self.menu_date = datetime.now()

    def test_create_menu(self):
        """
        Test menu creation
        """
        self.restaurant.save()
        menu = Menu(name=self.menu_name, date=self.menu_date, restaurant_id=self.restaurant.id)
        menu.save()
        self.assertIsNotNone(Menu.objects.filter(name=self.menu_name).first())


class MenuAPITestCase(APITestCase):
    """
    Test class to test Menu API
    """

    def setUp(self):
        self.apiClient = APIClient()
        self.restaurant_name = "restaurant name"
        self.restaurant = Restaurant(name=self.restaurant_name)
        self.restaurant.save()
        self.menu_name = "menu name"
        self.menu_date = datetime.now()

    def test_api_create_menu(self):
        """
        Test menu creation using API
        """

        menu_json = {
            'name': self.menu_name,
            'date': self.menu_date.strftime('%Y-%m-%d'),
            'restaurant': self.restaurant.id
        }
        response = self.client.post(reverse('menu'), menu_json, format="json")
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_api_get_menu(self):
        """
        Test menu retrieval using API
        """
        response = self.client.get(reverse('menu'))
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_api_get_menu_today(self):
        """
        Test menu retrieval for today using API
        """
        response = self.client.get(reverse('menu-today'))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
