from django.shortcuts import render
from .models import LogEntry, ReadingLogEntry, ListeningLogEntry
from rest_framework import generics
from .serializers import ReadingLogEntrySerializer, ListeningLogEntrySerializer

# Create your views here.

# class LogEntryList(generics.ListAPIView):
#     queryset = LogEntry.objects.all()
#     serializer_class = ReadingLogEntrySerializer

# Reading
class ReadingLogEntryCreate(generics.CreateAPIView):
    queryset = ReadingLogEntry.objects.all()
    serializer_class = ReadingLogEntrySerializer

class ReadingLogEntryList(generics.ListAPIView):
    queryset = ReadingLogEntry.objects.all()
    serializer_class = ReadingLogEntrySerializer

class ReadingLogEntryDetail(generics.RetrieveAPIView):
    queryset = ReadingLogEntry.objects.all()
    serializer_class = ReadingLogEntrySerializer

class ReadingLogEntryUpdate(generics.RetrieveUpdateAPIView):
    queryset = ReadingLogEntry.objects.all()
    serializer_class = ReadingLogEntrySerializer

class ReadingLogEntryDelete(generics.RetrieveDestroyAPIView):
    queryset = ReadingLogEntry.objects.all()
    serializer_class = ReadingLogEntrySerializer

# Listening
class ListeningLogEntryCreate(generics.CreateAPIView):
    queryset = ListeningLogEntry.objects.all()
    serializer_class = ListeningLogEntrySerializer

class ListeningLogEntryList(generics.ListAPIView):
    queryset = ListeningLogEntry.objects.all()
    serializer_class = ListeningLogEntrySerializer

class ListeningLogEntryDetail(generics.RetrieveAPIView):
    queryset = ListeningLogEntry.objects.all()
    serializer_class = ListeningLogEntrySerializer

class ListeningLogEntryUpdate(generics.RetrieveUpdateAPIView):
    queryset = ListeningLogEntry.objects.all()
    serializer_class = ListeningLogEntrySerializer

class ListeningLogEntryDelete(generics.RetrieveDestroyAPIView):
    queryset = ListeningLogEntry.objects.all()
    serializer_class = ListeningLogEntrySerializer