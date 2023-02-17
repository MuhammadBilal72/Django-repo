from django.contrib import admin
from django.urls import path,include
from core import views
from login import views as lv
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('my/',include('skills.urls')),
    path('my/',include("contact.urls")),
    path('login/',lv.login)
]
