from rest_framework import serializers

from api.models.menu import Menu


class MenuSerializer(serializers.ModelSerializer):
    """
    Menu serializer
    """

    class Meta:
        model = Menu
        fields = '__all__'
