from rest_framework import serializers
from .models import PredictModel

class PredictModelSerializer(serializers.Serializer):
    class Meta():
        model = PredictModel
        fields = ["img"]