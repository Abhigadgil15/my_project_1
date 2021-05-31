from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    response = render(request, 'index.html' )
    
    return response
