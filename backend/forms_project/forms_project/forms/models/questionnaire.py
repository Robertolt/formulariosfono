
from django.db import models
from django.utils import timezone

class Questionnaire(models.Model):
    title = models.TextField()
    description = models.TextField(default='')
    created_at = models.DateTimeField(default=timezone.now)
