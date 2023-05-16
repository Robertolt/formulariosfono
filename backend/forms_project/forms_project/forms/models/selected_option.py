
from django.db import models
from django.utils import timezone

from .question_option import QuestionOption
from .response import Response


class SelectedOption(models.Model):        
    response = models.ForeignKey(Response, on_delete=models.CASCADE)
    question_option = models.ForeignKey(QuestionOption, on_delete=models.SET_NULL, null=True)
    updated_at = models.DateTimeField(default=timezone.now)
