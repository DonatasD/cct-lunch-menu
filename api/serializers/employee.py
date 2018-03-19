from rest_framework import serializers

from api.models.employee import Employee
from api.serializers.vote import VoteSerializer


class EmployeeSerializer(serializers.ModelSerializer):
    """
    Employee serializer
    """
    votes = VoteSerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = '__all__'
