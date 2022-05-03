from django.shortcuts import render
from .models import Media
from rest_framework import generics
from .serializers import MediaSerializer

# Create your views here.
# POST - Single Media
class MediaCreate(generics.CreateAPIView):
    queryset = Media.objects.all(),
    serializer_class = MediaSerializer

# GET - All Media
class MediaList(generics.ListAPIView):
    queryset = Media.objects.all(),
    serializer_class = MediaSerializer

# GET - Single Media
class MediaDetail(generics.RetrieveAPIView):
    queryset = Media.objects.all(),
    serializer_class = MediaSerializer

# UPDATE - Single Media
class MediaUpdate(generics.RetrieveUpdateAPIView):
    queryset = Media.objects.all(),
    serializer_class = MediaSerializer

# DELETE - Single Media
class MediaDelete(generics.RetrieveDestroyAPIView):
    queryset = Media.objects.all(),
    serializer_class = MediaSerializer