# console/serializers.py
from rest_framework import serializers
from .models import ClassifiedWaterFlowData

class ClassifiedWaterFlowDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassifiedWaterFlowData
        fields = '__all__'
