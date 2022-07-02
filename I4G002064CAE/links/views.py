from django.shortcuts import render
from rest_framework import generics
#from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .serializers import LinkSerializer
from .models import Link

class LinkListApi(generics.ListAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class LinkDetailApi(generics.RetrieveAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class LinkCreateApi(generics.CreateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class LinkUpdateApi(generics.UpdateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class LinkDeleteApi(generics.DestroyAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

# Create your views here.
