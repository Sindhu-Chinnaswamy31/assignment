from django.shortcuts import render
from django.http import HttpResponse

def reg(request):
    return render(request,'register.html')
