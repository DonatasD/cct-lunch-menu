from datetime import datetime

from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient

from api.models.employee import Employee
from api.models.menu import Menu
from api.models.restaurant import Restaurant
from api.models.vote import Vote


class VoteTestCase(TestCase):
    """
    Test class to test Vote model
    """

    def setUp(self):
        self.restaurant_name = "restaurant name"
        self.restaurant = Restaurant(name=self.restaurant_name)
        self.menu_name = "menu name"
        self.menu_date = datetime.now()
        self.employee_name = "employee name"
        self.employee = Employee(name=self.employee_name)
        self.employee.save()
        self.restaurant.save()
        self.menu = Menu(name=self.menu_name, date=self.menu_date, restaurant_id=self.restaurant.id)
        self.menu.save()

    def test_create_vote(self):
        """
        Test menu creation
        """
        vote = Vote(menu=self.menu, employee=self.employee)
        vote.save()
        self.assertIsNotNone(Vote.objects.filter(menu=self.menu, employee=self.employee).first())


class VoteAPITestCase(APITestCase):
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
        self.menu = Menu(name=self.menu_name, date=self.menu_date, restaurant_id=self.restaurant.id)
        self.menu.save()
        self.employee_name = "employee name"
        self.employee = Employee(name=self.employee_name)
        self.employee.save()

    def test_api_create_vote(self):
        """
        Test menu creation using API
        """
        vote_json = {'menu': self.menu.id, 'employee': self.employee.id}
        response = self.client.post(reverse('vote'), vote_json, format="json")
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_api_get_vote(self):
        """
        Test menu retrieval using API
        """
        response = self.client.get(reverse('vote'))
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_api_get_today_vote_result(self):
        """
        Test menu retrieval for today using API
        """
        response = self.client.get(reverse('vote-today-result'))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
