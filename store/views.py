from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from rest_framework import generics
from .serializers import StoreSerializer
from .models import Store


class StoreDetailView(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer    

