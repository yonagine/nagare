from django.contrib import admin
from .models import ReadingLogEntry, ListeningLogEntry

# Register your models here.
admin.register(ReadingLogEntry)
admin.register(ListeningLogEntry)