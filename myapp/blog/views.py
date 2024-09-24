from django.shortcuts import render, get_object_or_404
from .models import Blogs

# Create your views here.

def blogs(request):
    all_blog = Blogs.objects.all()
    return render(request, 'blog/blog.html', {'blogs': all_blog})

def description(request, blog_id):
    blog=get_object_or_404(Blogs, pk=blog_id)
    return render(request, 'blog/blog_description.html',{'Blog': blog})