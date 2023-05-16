
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .questionnaire import Questionnaire


class Question(models.Model):
    class QuestionType(models.TextChoices):
        RADIO = "RD", _("Multiple Choice")
        CHECK = "CK", _("Multiple Answer")
        TEXT = "TX", _("Written Answer")
        
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    question_type = models.CharField(
        max_length=2,
        choices=QuestionType.choices,
        default=QuestionType.RADIO,
    )


"""
class Opcao(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    texto_resposta = models.TextField(max_length=300)
    NUMERO_ALTERNATIVA = (
        (0, 'Nunca'),
        (1, 'Raramente'),
        (2, 'Ocasionalmente'),
        (3, 'Frequentemente'),
        (4, 'Sempre'),

    )
    numero_alternativa = models.IntegerField(max_length=1, choices=NUMERO_ALTERNATIVA)

class RespostaQuestionario(models.Model):
    nome_paciente = models.CharField(max_length=60)
    cpf_paciente = models.IntegerField(max_length=11, unique=True)
    data_resposta = models.DateField()


class RespostaPergunta(models.Model):
    respostaquestionario = models.ForeignKey(RespostaQuestionario, on_delete=models.CASCADE)
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    opcao = models.ForeignKey(Opcao, on_delete=models.CASCADE)
"""
