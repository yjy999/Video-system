from rest_framework import serializers
from .models import Video,mainPage

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Video
        fields='__all__'

class mainPageSerializer(serializers.ModelSerializer):
    class  Meta:
        model=mainPage
        fields='__all__'