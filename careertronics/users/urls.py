from django.urls import path, include
from. import views

urlpatterns = [
    path("", views.IndexView,name="index"),
    path('about', views.AboutView, name="about"),
    path('contact', views.ContactView, name="contact"),
    path('cancel', views.CancelView, name="cancel"),
    path('policy', views.PolicyView, name="policy"),
    path('terms', views.TermsView, name="terms"),
    path('shipping', views.ShippingView, name="shipping"),
    
    
]
