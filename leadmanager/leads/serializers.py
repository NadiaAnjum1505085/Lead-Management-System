from .models import Subordinate
from rest_framework import serializers

class SubordinateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subordinate
        fields = '__all__'
