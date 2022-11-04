from django.shortcuts import render,redirect
from blog.models import Blog
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
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

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        message = ""
        if pass1 == pass2:
            user = User(username=username)
            user.set_password(pass1)
            user.save()
            msg="Save successfully"
            messages.add_message(request,messages.SUCCESS,msg)
            return redirect('signin')
        else:
            msg="Password and Password Confirmation does not match"
            messages.add_message(request,messages.ERROR,msg)
            return redirect('signup')
    else:
        return render(request,'signup.html')

def signin(request):
    if request.method=='POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        user = authenticate(username=username,password=pass1)
        if user is None:
            msg = "username and password does not match"
            messages.add_message(request,messages.ERROR,msg)
        else:
            login(request,user)
            return redirect('dashboard')
    return render(request,'signin.html')


def dashboard(request):
    if request.user.is_authenticated:
        return render(request,'dashboard.html')
    else:
        return redirect('signin')

def signout(request):
    logout(request)
    return redirect('signin')