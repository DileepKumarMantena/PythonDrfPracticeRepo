from .models import RegistrationModel

from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrationModel
        fields = '__all__'

