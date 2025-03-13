from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def context(request):
    return render(request, 'context.html')

def contact(request):
    return render(request, 'contact.html')

def service(request):
    return render(request, 'service.html')

def service(request):
    return render(request, 'signup.html')

