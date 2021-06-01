from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    developed_by = "Prateek"
    mentors = [
    "Abhinav Gadgil",
    "Rahul Mandviya",
    "Yash Kulkarni"
    ]
    context = {
        "developer": developed_by,
        "mentors": mentors
    }
    response = render(request, 'index.html', context )
    
    return response
