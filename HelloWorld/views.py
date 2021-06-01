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
    show_developer = True
    context = {
        "developer": developed_by,
        "mentors": mentors,
        "show_developer": show_developer
    }
    response = render(request, 'HelloWorld/index.html', context )
    
    return response
