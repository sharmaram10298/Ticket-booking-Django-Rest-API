from rest_framework import serializers
from .models import *



class TheaterSerializer(serializers.ModelSerializer):

    class Meta:
        model  = Theater
        fields = '__all__'