import logging
from datetime import datetime

from django.db.models import Count
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models.vote import Vote
from api.serializers.vote import VoteSerializer

logger = logging.getLogger(__name__)


class VoteView(generics.ListCreateAPIView):
    """
    Vote API
    """
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

    @api_view(['GET'])
    def today_result(self):
        votes = Vote.objects.filter(menu__date=datetime.today().date()).values('menu').annotate(count=Count('menu__id'))
        return Response(votes)
