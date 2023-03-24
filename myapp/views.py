from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Theater
from .serializers import TheaterSerializer

# Create your views here.


class TheaterList(APIView):


    def get(self, request):
        thearter = Theater.objects.all()
        serializer=TheaterSerializer(thearter, many=True)
        return Response(serializer.data)


    def post(self, request):
        thearter = Theater.objects.all()
        serializer=TheaterSerializer(thearter, many=True)
        return Response(serializer.data)
