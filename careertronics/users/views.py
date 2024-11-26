from django.shortcuts import render

# Create your views here.
def IndexView(request):
    return render(request,"users/index.html")


def AboutView(request):
    return render(request,"users/about.html")


def ContactView(request):
    return render(request,"users/contact.html")