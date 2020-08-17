from django.db import models
import tempfile

from django.core.files import File


# Create your models here.
class Song(models.Model):
    artist = models.IntegerField()
    title = models.CharField(max_length=200, blank=True)
    audio = models.FileField(upload_to='uploads/', blank=True)

    def __str__(self):
        return self.title
