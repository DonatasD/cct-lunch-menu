from rest_framework import serializers


class ResultSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    menu_id = serializers.IntegerField()


class ResultListSerializer(serializers.Serializer):
    results = ResultSerializer(many=True)
    date = serializers.DateField()
