from django.shortcuts import render
from django.http import HttpResponse

def index (request):
    return HttpResponse("Nasa APP")

def specific(request):
    return HttpResponse("This is the specific URL")

def article(request,article_id):
    return HttpResponse(article_id)
