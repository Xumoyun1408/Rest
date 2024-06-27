from rest_framework import serializers
from .models import Travel, Klass, Mehmonhona
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

import io

class TravelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    content = serializers.CharField()
    period = serializers.DateTimeField(read_only=True)
    price = serializers.IntegerField()
    klass = serializers.CharField()
    mehmonhona = serializers.CharField()

    def create(self, validated_data):
        return Travel().objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.content = validated_data.get('content',instance.content)
        instance.period = validated_data.get('period',instance.period)
        instance.price = validated_data.get('price',instance.price)
        instance.klass = validated_data.get('klass',instance.klass)
        instance.mehmonhona = validated_data.get('mehmonhona',instance.mehmonhona)
        instance.save()
        return instance

class MehmonhonaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    price = serializers.IntegerField()

class KlassSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    price = serializers.IntegerField()
