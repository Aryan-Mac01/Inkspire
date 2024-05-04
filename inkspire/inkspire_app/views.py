from django.shortcuts import render

# Create your views here.
posts = [
    {
        'author': 'AryanMac',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': '30 April, 2024'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': '1 May, 2024'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})   