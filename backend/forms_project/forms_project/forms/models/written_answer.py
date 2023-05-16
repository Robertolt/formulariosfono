
from django.db import models
from django.utils import timezone

from .question import Question
from .response import Response


class WrittenAnswer(models.Model):        
    response = models.ForeignKey(Response, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True)
    text = models.TextField()
    updated_at = models.DateTimeField(default=timezone.now)
