from rest_framework import serializers

from api.models.restaurant import Restaurant
from api.serializers.menu import MenuSerializer


class RestaurantSerializer(serializers.ModelSerializer):
    """
    Restaurant serializer
    """
    menus = MenuSerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = '__all__'
