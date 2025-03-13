from django.test import TestCase
from django.shortcuts import render

# Create your tests here.
def home(request):
    return render(request, 'home.html')

def upload(request):
    return render(request, 'upload.html')

def view_data(request):
    return render(request, 'view_data.html')