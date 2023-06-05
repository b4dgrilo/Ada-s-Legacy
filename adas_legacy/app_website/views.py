from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context

# Create your views here

#chamando html
def index(request):
    # documentoExterno = open("C:/Users/babi7/OneDrive/Área de Trabalho/Ada-s-Legacy/adas_legacy/app_website/templates/index.html")
    # pagina = Template(documentoExterno.read())
    # documentoExterno.close()
    # ctx = Context()
    # documento = pagina.render(ctx)
    # return HttpResponse(documento)

    return render(request, 'index.html')


def cadastro(request):
    # documentoExterno = open("C:/Users/babi7/OneDrive/Área de Trabalho/Ada-s-Legacy/adas_legacy/app_website/templates/cadastro.html")
    # pagina = Template(documentoExterno.read())
    # documentoExterno.close()
    # ctx = Context()
    # documento = pagina.render(ctx)
    # return HttpResponse(documento)

    return render(request, 'cadastro.html')

def login(request):
    # documentoExterno = open("C:/Users/babi7/OneDrive/Área de Trabalho/Ada-s-Legacy/adas_legacy/app_website/templates/login.html")
    # pagina = Template(documentoExterno.read())
    # documentoExterno.close()
    # ctx = Context()
    # documento = pagina.render(ctx)
    # return HttpResponse(documento)

    return render(request, 'login.html')
    