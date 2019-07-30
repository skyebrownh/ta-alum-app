# from django.shortcuts import render
from django.http import HttpResponse

def landingPage(request):
  return HttpResponse('<h1>landing page: hello world</h1>')