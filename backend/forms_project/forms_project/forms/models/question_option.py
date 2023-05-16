
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .question import Question


class QuestionOption(models.Model):        
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
