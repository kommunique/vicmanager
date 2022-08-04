from django.shortcuts import  render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this

# Create your views here.

def home_page(request):
    return render(request, 'gamesessions/index.html')
