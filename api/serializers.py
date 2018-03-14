from rest_framework import serializers
from .models import Employee, Restaurant


# Employee Serializer
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'name')


# Restaurant Serializer
class RestaurantSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'name')