from django.db import models

# Create your models here.


class Questionario(models.Model):
    titulo_questionario = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)


class Pergunta(models.Model):
    questionario = models.ForeignKey(Questionario, on_delete=models.CASCADE)
    texto_pergunta = models.TextField(max_length=300)


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
