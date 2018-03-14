from rest_framework import generics
from .serializers import EmployeeSerializer, RestaurantSerialiser
from .models import Employee, Restaurant
import logging

logger = logging.getLogger(__name__)


class EmployeeView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def perform_create(self, serializer):
        serializer.save()


class RestaurantView(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerialiser

    def perform_create(self, serializer):
        serializer.save()
