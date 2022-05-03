from django.shortcuts import render
from .models import Media
from rest_framework import generics
from .serializers import MediaSerializer

# Create your views here.
class MediaCreate(generics.CreateAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

class MediaList(generics.ListAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

class MediaDetail(generics.RetrieveAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

class MediaUpdate(generics.RetrieveUpdateAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

class MediaDelete(generics.RetrieveDestroyAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer