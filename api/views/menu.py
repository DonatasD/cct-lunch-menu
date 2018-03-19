import logging
from datetime import datetime

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models.menu import Menu
from api.serializers.menu import MenuSerializer

logger = logging.getLogger(__name__)


class MenuView(generics.ListCreateAPIView):
    """
    Menu API
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    @api_view(['GET'])
    def today(self):
        today_menu = Menu.objects.filter(date=datetime.today().date())
        serializer = MenuSerializer(today_menu, many=True)
        return Response(serializer.data)
