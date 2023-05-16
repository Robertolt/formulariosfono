
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from .questionnaire import Questionnaire


class Response(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
