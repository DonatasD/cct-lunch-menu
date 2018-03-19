from rest_framework import serializers

from api.models.vote import Vote


class VoteSerializer(serializers.ModelSerializer):
    """
    Vote serializer
    """

    class Meta:
        model = Vote
        fields = '__all__'
