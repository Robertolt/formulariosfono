from django.db import models
from django.utils import timezone
from .question import Questionario
from .users import User


class RespostaQuestionario(models.Model):
    questionario = models.ForeignKey(Questionario, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data_resposta = models.DateTimeField(default=timezone.now)
