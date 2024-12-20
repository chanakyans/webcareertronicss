from django.shortcuts import render

# Create your views here.
def IndexView(request):
    return render(request,"users/index.html")


def AboutView(request):
    return render(request,"users/about.html")


def ContactView(request):
    return render(request,"users/contact.html")


def CancelView(request):
    return render(request,"users/cancel.html")


def PolicyView(request):
    return render(request,"users/policy.html")


def TermsView(request):
    return render(request,"users/terms.html")


def ShippingView(request):
    return render(request,"users/shipping.html")