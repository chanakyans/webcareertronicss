from django.urls import path, include
from. import views

urlpatterns = [
    path("", views.IndexView,name="index"),
    path('about', views.AboutView, name="about"),
    path('contact', views.ContactView, name="contact"),
    
    
]
