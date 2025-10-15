from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {   
    'author': 'John Doe',
    'title': 'Blog Post 1',
    'content': 'First post content',
    'date_posted': 'April 20, 2025'
    },
    {
    'author': 'Jane Smith', 
    'title': 'Blog Post 2',
    'content': 'Second post content',
    'date_posted': 'April 21, 2025'
    }
]

def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')
