from django.http import HttpResponse


def index(request):
    return HttpResponse("HELLO! WORLD!")


def another(request):
    return HttpResponse("ANOTHER PAGE")
