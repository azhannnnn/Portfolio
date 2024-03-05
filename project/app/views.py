from django.shortcuts import render
from .models import User

# Create your views here.


def index(request):
    return render(request,'index.html')

def resume(request):
    return render(request,'resume.html')

def blog(request):
    return render(request,'blog.html')

def portfolio(request):
    return render(request,'portfolio.html')

def contact(request):
    return render(request,'contact.html')

def send(request):
    name = request.GET.get('name')
    email = request.GET.get('email')
    message = request.GET.get('message')
    

    User.objects.create(
        Name = name,
        Email = email,
        Message = message
    )
    msg = "Send Successfully"
    return render(request,'contact.html',{"msg":msg})


