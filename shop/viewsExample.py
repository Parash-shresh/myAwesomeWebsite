from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def displayMessage(request):
    return HttpResponse("index shoping")
def includeFunction(request):
    return HttpResponse("include function le kam aaru lai dinxa.")

