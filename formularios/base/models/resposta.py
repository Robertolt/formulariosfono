from django.db import models
from .resposta_questionario import RespostaQuestionario
from .question import Pergunta


class Resposta(models.Model):
    resposta_questionario = models.ForeignKey(RespostaQuestionario, on_delete=models.CASCADE)
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    opcao = models.CharField(max_length=64)

