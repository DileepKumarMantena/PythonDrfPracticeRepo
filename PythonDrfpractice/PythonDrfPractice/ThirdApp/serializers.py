from rest_framework import serializers
from .models import *
from .bmi import bmiweight


class ConverterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bodymass
        fields = ['id', 'name', 'height', 'weight']

    def create(self, validated_data):
        height = validated_data['height']
        weight = validated_data['weight']
        print(type(height))
        convert = bmiweight(height, weight)
        user = Bodymass.objects.create(name=validated_data['name'], height=height,
                                       weight=weight, bmi=convert)
        user.save()
        return user


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bodymass
        fields = ["id", 'name', 'height', 'weight', 'bmi']
