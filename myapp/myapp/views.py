from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Welcome to the Home Page")
    return render(request, 'web/index.html')

def about(request):
    return render(request, 'web/about.html')

def contact(responce):
    return HttpResponse("This is the Contact Page")