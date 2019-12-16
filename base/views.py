from django.shortcuts import render, redirect
from django.urls import reverse

def base(request):
    return render(request, 'base2.html')
