from django.http import HttpResponse


def home(request):
    return HttpResponse("Home")


def contact(request):
    return HttpResponse("Contato")


def about(request):
    return HttpResponse("Sobre")
# Create your views here.
