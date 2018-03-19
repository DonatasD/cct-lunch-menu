import logging

from rest_framework import generics

from api.models.restaurant import Restaurant
from api.serializers.restaurant import RestaurantSerializer

logger = logging.getLogger(__name__)


class RestaurantView(generics.ListCreateAPIView):
    """
    Restaurant API
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def perform_create(self, serializer):
        serializer.save()
