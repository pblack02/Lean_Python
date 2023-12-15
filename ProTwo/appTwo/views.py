from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("<em>My second app</em>")


def help(request):
    help_dict = {'help_insert': "Help Page"}
    return render(request, "appTwo/help.html", context=help_dict)

