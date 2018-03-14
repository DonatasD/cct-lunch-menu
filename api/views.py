from rest_framework import generics
from .serializers import EmployeeSerializer
from .models import Employee
import logging

logger = logging.getLogger(__name__)


class EmployeeView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def perform_create(self, serializer):
        serializer.save()

