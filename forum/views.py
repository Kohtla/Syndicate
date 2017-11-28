from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Welcome to FORUM!</h1>")

# Create your views here.
