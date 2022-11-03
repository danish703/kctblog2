from django.shortcuts import render
from blog.models import Blog
def home(request):
    blogs = Blog.objects.all() #select * from blogs
    context = {
        'blogs':blogs
    }
    return render(request,'index.html',context)

def details(request,id):
    blog = Blog.objects.get(pk=id)
    context = {
        'blog':blog
    }
    return render(request,'details.html',context)