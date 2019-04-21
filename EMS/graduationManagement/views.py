from django.shortcuts import render
from django.http import HttpResponse


def welcome(request):
    return render(request, 'graduationManagement/welcome.html')
<<<<<<< HEAD
=======


def func(request):
    return HttpResponse("func")
>>>>>>> b12887070dca45507f23fcc57d4d880354fe094e
