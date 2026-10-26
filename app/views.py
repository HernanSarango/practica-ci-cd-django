from django.http import HttpResponse


def inicio(request):
    return HttpResponse("Proyecto Django funcionando correctamente - Practica CI/CD")
