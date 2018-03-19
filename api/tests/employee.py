from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from api.models.employee import Employee


class EmployeeTestCase(TestCase):
    """
    Test class to test Employee model
    """

    def setUp(self):
        self.employee_name = "employee name"
        self.employee = Employee(name=self.employee_name)

    def test_create_employee(self):
        """
        Test employee creation
        """
        self.employee.save()
        self.assertIsNotNone(Employee.objects.filter(name=self.employee_name).first())


class EmployeeAPITestCase(APITestCase):
    """
    Test class to test Employee API
    """

    def setUp(self):
        self.employee_name = "employee name"
        self.employee_json = {'name': self.employee_name}

    def test_api_create_employee(self):
        """
        Test employee creation using API
        """
        response = self.client.post(reverse('employee'), self.employee_json, format="json")
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_api_get_employees(self):
        """
        Test employee retrieval using API
        """
        response = self.client.get(reverse('employee'))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
