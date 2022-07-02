from django.db import models
from django.utils import timezone

# Create your models here.

class Resource(models.Model):
    name = models.CharField(max_length=36, default=None, null=True)
    link = models.URLField()

