from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegisteration
from .models import User
# Create your views here.
def add_show(request):
    if request.method=="POST":
        frm=StudentRegisteration(request.POST)
        if frm.is_valid():
            nm=frm.cleaned_data["name"]
            em=frm.cleaned_data["email"]
            pw=frm.cleaned_data["password"]
            reg=User(name=nm,email=em,password=pw)
            reg.save()
            frm=StudentRegisteration()
    else:
        frm=StudentRegisteration()
    students=User.objects.all()
    return render(request,'enroll/addandshow.html',{"form":frm,"stu":students})


# Deleting the data 
def delete_data(request,id):
    print(request.method)
    if request.method=="POST":
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect("/")


#This Fucntion Will Update Data
def update_data(request,id):
    if request.method=="POST":
        pi=User.objects.get(pk=id)
        frm=StudentRegisteration(request.POST,instance=pi)
        frm.save()
    else:
        pi=User.objects.get(pk=id)
        frm=StudentRegisteration(instance=pi)
        
    return render(request,"enroll/updatestudent.html",{"frm":frm})

    