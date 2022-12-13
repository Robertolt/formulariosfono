from django.http import HttpResponse
from django.shortcuts import render

# from django.shortcuts import render
from .models import Questionario, Pergunta


# Create your views here.
def home(request):
    q = Questionario.objects.first()
    p = Pergunta.objects.filter(questionario=q).all()
    context = {
        'questionario': q,
        'perguntas': p,
    }
    erros = {}
    if request.method == 'POST':
        name = request.POST
        print(name)
        print(p)
        # for i in range(len(p)):
        # valor = name['i']
        # print(valor)

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
