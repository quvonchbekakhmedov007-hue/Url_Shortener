from rest_framework import serializers
from .models import Shorturl

class ShorturlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shorturl
        fields = ['original_url']



class ShorturlDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shorturl
        fields = '__all__'