from rest_framework import serializers
from .models import ReadingLogEntry, ListeningLogEntry
from media.models import Media

class LogEntrySerializer(serializers.Serializer):
    created = serializers.DateField(read_only=True)
    notes = serializers.CharField()
    log_time = serializers.TimeField()
    media_pk = serializers.PrimaryKeyRelatedField(queryset=Media.objects.all())

    class Meta:
        fields = ['pk', 'created', 'notes', 'log_time', 'media_pk']

class ReadingLogEntrySerializer(LogEntrySerializer, serializers.ModelSerializer):
    class Meta:
        model = ReadingLogEntry
        fields = LogEntrySerializer.Meta.fields + ['characters', 'lines']

class ListeningLogEntrySerializer(LogEntrySerializer, serializers.ModelSerializer):
    class Meta:
        model = ListeningLogEntry
        fields = LogEntrySerializer.Meta.fields
