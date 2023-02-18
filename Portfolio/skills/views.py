from django.shortcuts import render
from .models import Skills
# Create your views here.
def skills(request):
   
    return render(request,'skills/skills.html',{'skills':'active'})
