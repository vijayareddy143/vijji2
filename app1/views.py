from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def vijji1(request):
    return HttpResponse('<h1>hi vijji</h1>')

def vijji2(request):
    return HttpResponse('<h2>she is very good girl</h1>')