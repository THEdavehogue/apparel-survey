from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'survey_app/home.html')
    return HttpResponse("Welcome to the Giant Denver Apparel Survey!")
