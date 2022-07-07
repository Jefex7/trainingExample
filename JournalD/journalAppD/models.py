from django.db import models
from django.utils import timezone


# Create your models here.

class Resource(models.Model):
    title = models.CharField(max_length=600, default=None, null=True)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


