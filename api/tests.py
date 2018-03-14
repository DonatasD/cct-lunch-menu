from django.test import TestCase
from .models import Employee
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse


# Test class to test Employee model
class EmployeeModelTestCase(TestCase):
    def setUp(self):
        self.employee_name = "test name"
        self.employee = Employee(name=self.employee_name)

    def test_create_employee(self):
        self.employee.save()
        self.assertIsNotNone(Employee.objects.filter(name=self.employee_name).first())


class EmployeeViewTestCase(TestCase):
    def setUp(self):
        self.apiClient = APIClient()
        self.employee_name = "test name in json"
        self.employee_json = {'name': self.employee_name}

    def test_api_create_employee(self):
        response = self.client.post(reverse('employee'), self.employee_json, format="json")
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_api_get_employees(self):
        response = self.client.get(reverse('employee'))
        self.assertEquals(response.status_code, status.HTTP_200_OK)

