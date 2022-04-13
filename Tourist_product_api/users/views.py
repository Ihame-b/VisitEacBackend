from email import message
from itertools import product
from urllib.request import Request
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from Papi.models import Product



# Create your views here.
def home(request):
    all_product = Product.objects.all()
    return render(request, 'users/home.html', {'product': all_product})

def register(request):
    if request.method =="POST":
       form =UserRegisterForm(request.POST)
       if form.is_valid():
           form.save()
           username = form.cleaned_data.get('username')
           messages.success(request, f'Hi {username}, your account was created successfully')
           return redirect('home')
    else:
        form = UserRegisterForm()       
    return render(request, 'users/register.html', {'form':form})    

@login_required
def profile(request):
    return render(request, 'users/profile.html')

def feedback(request):
    return render(request, 'users/EAC_Tourist_Feedback_Form.html')   

def aboutuslab(request):
    return render(request, 'users/aboutulab.html')