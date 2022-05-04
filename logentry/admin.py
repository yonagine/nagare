from django.contrib import admin
from .models import ReadingLogEntry, ListeningLogEntry

# Register your models here.
admin.site.register(ReadingLogEntry)
admin.site.register(ListeningLogEntry)