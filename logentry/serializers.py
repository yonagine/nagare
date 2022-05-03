from rest_framework import serializers
from .models import LogEntry, ReadingLogEntry, ListeningLogEntry

class LogEntrySerializer(serializers.Serializer):
    pk = serializers.CharField()
    created = serializers.CharField()
    notes = serializers.CharField()
    log_time = serializers.CharField()
    fk = serializers.CharField()

    class Meta:
        model = LogEntry
        fields = ['pk', 'created', 'notes', 'log_time', 'fk']

class ReadingLogEntrySerializer(LogEntrySerializer, serializers.ModelSerializer):
    class Meta:
        model = ReadingLogEntry
        fields = LogEntrySerializer.Meta.fields + ['characters', 'lines']

class ListeningLogEntrySerializer(LogEntrySerializer, serializers.ModelSerializer):
    class Meta:
        model = ListeningLogEntry
        fields = LogEntrySerializer.Meta.fields
