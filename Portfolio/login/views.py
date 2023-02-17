from django.shortcuts import render
from .forms import LoginForm

# Create your views here.
def login(request):

    frm=LoginForm(request.POST)
    if request.method=="POST":
        # checking wether data is valid or not
        if frm.is_valid():
            print("Password",frm.cleaned_data['password'])
    else:
        frm=LoginForm()

    return render(request,'login/login.html',{'form':frm})