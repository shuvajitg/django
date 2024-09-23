from django.shortcuts import render
from .models import Blogs

# Create your views here.

def blogs(request):
    all_blog = Blogs.objects.all()
    return render(request, 'blog/blog.html', {'blogs': all_blog})
