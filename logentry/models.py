from django.db import models
from media.models import Media

# Create your models here.
class LogEntry(models.Model):
    created = models.DateField(auto_now_add=True)
    notes = models.TextField("notes", max_length=240)
    log_time = models.TimeField()
    media_pk = models.ForeignKey(Media, on_delete=models.RESTRICT)

    class Meta:
        abstract = True

class ReadingLogEntry(LogEntry):
    characters = models.IntegerField()
    lines = models.IntegerField()
    
class ListeningLogEntry(LogEntry):
    pass