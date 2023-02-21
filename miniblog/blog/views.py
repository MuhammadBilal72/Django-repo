from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import SignupForm,LoginForm,PostForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from .models import Post
from django.contrib.auth.models import Group


# Home Page
def home(request):
    posts=Post.objects.all()
    return render(request,"blog/home.html",{"posts":posts})


# ABout Page
def about(request):
    return render(request,"blog/about.html")


# Contact Page
def contact(request):
    return render(request,"blog/contact.html")


# Login Page
def user_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            frm=LoginForm(request=request,data=request.POST)
            if frm.is_valid():
                uname=frm.cleaned_data["username"]
                upass=frm.cleaned_data["password"]
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,"Successfully Logged in")
                    return HttpResponseRedirect("/dashboard/")
        else:
            frm=LoginForm()
        return render(request,"blog/login.html" ,{"form":frm})
    else:
        return HttpResponseRedirect("/dashboard/")


#Logout Page
def log_out(request):
    logout(request)
    return HttpResponseRedirect("/")


#Dashboard Page
def dashboard(request):
    if request.user.is_authenticated:
        posts=Post.objects.all()
        user =request.user
        fullname=user.get_full_name()
        gps=user.groups.all()
        
        return render(request,"blog/dashboard.html",{"posts":posts,"fullname":fullname,"groups":gps})
    else:
        return HttpResponseRedirect("/login/")


#Signup Page
def user_signup(request):
    if request.method=="POST":
        frm=SignupForm(request.POST)
        if frm.is_valid():
            messages.success(request,"Congratulations! You Are an Author Now.")
            user=frm.save()
            group=Group.objects.get(name="Authors")
            user.groups.add(group)
    else:
        frm=SignupForm()
    return render(request,"blog/signup.html",{"form":frm})


#Add post
def add_post(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            form=PostForm(request.POST)
            if form.is_valid():
                form.save()
                form=PostForm()
                messages.success(request,"Post Added Sucessfully")
        else:
            form=PostForm()
        return render(request,"blog/addpost.html",{"form":form})
    else:
        return HttpResponseRedirect("/login/")
    
    
    
# Update Post
def update_post(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            pi=Post.objects.get(pk=id)
            form=PostForm(request.POST,instance=pi)
            if form.is_valid():
                form.save()
                form=PostForm()
                messages.success(request,"Post Added Sucessfully")
        else:
            pi=Post.objects.get(pk=id)
            form=PostForm(instance=pi)
        return render(request,"blog/updatepost.html",{"form":form})
    else:
        return HttpResponseRedirect("/login/")
    
 
 
 
 #Delete Post   
def delete_post(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            pi=Post.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect("/dashboard/")
        return HttpResponseRedirect("/dashboard/")
    else:
        return HttpResponseRedirect("/login/")