
from typing import Any, Dict
from django.shortcuts import redirect

from django.http import HttpResponse
from django.shortcuts import render

# from django.shortcuts import render
from .models import Questionario, Pergunta
from .models import RespostaQuestionario, Resposta, User

from django.views.generic.edit import FormView
from django import forms

'''
class FormResposta(forms.Form):
    nome = forms.CharField(required=True)
    cpf = forms.CharField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        q = Questionario.objects.first()
        p = Pergunta.objects.filter(questionario=q).all()

        self.fields['questionario'] = forms.CharField(widget=forms.HiddenInput(), initial=q.id)

        CHOICES = [
            (0, "Nunca"),
            (1, "Raramente"),
            (2, "Ocasionalmente"),
            (3, "Frequentemente"),
            (4, "Sempre"),
        ]

        for pergunta in p:
            self.fields[pergunta.id] = forms.ChoiceField(
                label=pergunta.texto,
                widget=forms.RadioSelect,
                choices=CHOICES,
                required=True
            )

            print(kwargs)
            val = kwargs.pop(pergunta.id, None)
            print(pergunta.id, val)

            if val is not None:
                self.fields[pergunta.id].initial == val


class FormRespostaView(FormView):
    template_name = 'base/home.html'
    form_class = FormResposta
    success_url = 'sucesso'

    def form_valid(self, form):
        # fazer validacao do usuario
        # checar se todas as perguntas foram respondidas
        return super().form_valid(form)


def sucesso(request):
    render(request, 'base/sucesso.html')

'''


def resposta_questionario_view(request, pk):
    resposta_questionario = RespostaQuestionario.objects.filter(id=pk)

    if resposta_questionario.count() > 0:
        resposta_questionario = resposta_questionario.first()
    else:
        resposta_questionario = None

    return render(request, 'base/resposta_questionario.html', context={"resposta_questionario": resposta_questionario})


def sucesso(request):
    return render(request, 'base/sucesso.html')


def home(request):
    q = Questionario.objects.first()
    p = Pergunta.objects.filter(questionario=q).all()

    context = {
        'questionario': q,
        'perguntas': p,
    }

    erros = {}

    if request.method == 'POST':
        print(request.POST)

        # TODO: adicionar verificacao do cpf
        users = User.objects.filter(first_name=request.POST['nome'])

        if users.count() > 0:
            resp_quest = RespostaQuestionario(questionario=q, usuario=users.first())
            resp_quest.save()

            for pergunta in p:
                opcao = request.POST.get(str(pergunta.id), "")
                resposta = Resposta(resposta_questionario=resp_quest, pergunta=pergunta, opcao=opcao)
                resposta.save()

            return redirect(f'/sucesso')
            # return redirect(f'/resposta_questionario/{resp_quest.id}')

    #     for  in p.id:
    #         contador = 0
    #         nunca = request.POST.get('0 Nunca', None)
    #         if nunca is None:
    #             contador += 1
    #         raramente = request.POST.get('1 Raramente', None)
    #         if raramente is None:
    #             contador += 1
    #         frequentemente = request.POST.get('3 Frequentemente', None)
    #         if frequentemente is None:
    #             contador += 1
    #         ocasionalmente = request.POST.get('2 Ocasionalmente', None)
    #         if ocasionalmente is None:
    #             contador += 1
    #         sempre = request.POST.get('4 Sempre', None)
    #         if sempre is None:
    #             contador += 1
    #         if contador == 4:
    #             print(nunca, raramente, ocasionalmente, frequentemente, sempre)
    #         else:
    #             erros['e'] = 'Favor selecionar uma opção!'
    # if erros:
    #     context['erros'] = erros
    # else:
    #     pass
    return render(request, 'base/home.html', context=context)
