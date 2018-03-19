import logging

from rest_framework import generics

from api.models.employee import Employee
from api.serializers.employee import EmployeeSerializer

logger = logging.getLogger(__name__)


class EmployeeView(generics.ListCreateAPIView):
    """
    Employee API
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def perform_create(self, serializer):
        serializer.save()
