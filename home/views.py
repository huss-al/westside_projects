from django.shortcuts import render


# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'home/home.html')

def what_we_do(request):
    return render(request, 'home/what-we-do.html')

def gallery_view(request):
    return render(request, 'home/projects.html')

def about_view(request):
    return render(request, 'home/about.html')

def contact_view(request):
    return render(request, 'home/contact.html')
