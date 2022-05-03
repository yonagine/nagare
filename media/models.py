from django.db import models

# Create your models here.
class Media(models.Model):
    name = models.CharField("Name", max_length=240)
    description = models.TextField("Description", max_length=240)
    created = models.DateField(auto_now_add=True)

    VISUALNOVEL = 'VN'
    LIGHTNOVEL = 'LN'
    ANIME = 'AN'
    AUDIO = 'AU'
    UNKNOWN = 'NA'

    KIND_CHOICES = [
        ('Reading', (
                (VISUALNOVEL, 'Visual Novel'),
                (LIGHTNOVEL, 'Light Novel'),
            )
        ),
        ('Listening', (
                (ANIME, 'Anime'),
                (AUDIO, 'Audio'),
            )
        ),
        (UNKNOWN, 'Unknown'),
    ]

    kind = models.CharField(
        max_length=2,
        choices=KIND_CHOICES,
        default=UNKNOWN,
    )

    def __str__(self):
        return self.name

class ReadingMedia(Media):
    pass

class ListeningMedia(Media):
    pass