from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def mouni(request):
    return HttpResponse('<h1><marquee>she is my frd</h1></marquee>')

def mounika(request):
    return HttpResponse('<h1><marquee>MOUNI VIJJI ARE BEST frd</h1></marquee>')

