import logging
from datetime import datetime

from django.db.models import Count
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models.vote import Vote
from api.serializers.result import ResultListSerializer
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
        today = datetime.today().date()
        qs = Vote.objects\
            .filter(menu__date=today)\
            .values('menu_id')\
            .annotate(count=Count('menu__id'))\
            .order_by('-count')
        results = {
            "date": today,
            "results": list(qs)
        }
        results_serializer_data = ResultListSerializer(results).data
        logger.info("Generated today results: {0}".format(results_serializer_data))
        return Response(results_serializer_data)
