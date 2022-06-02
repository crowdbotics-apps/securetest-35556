from django.conf import settings
from django.db import models


class Crowd(models.Model):
    "Generated Model"
    name = models.TextField()
    email = models.TextField(
        null=True,
        blank=True,
    )
