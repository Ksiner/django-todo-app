from django.http import HttpResponse, HttpRequest

def index(request: HttpRequest):
    return HttpResponse("Hello, world. You're at the polls index.")