from rest_framework import serializers
from .models import Project, Measurement


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class MeasurmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = "__all__"
