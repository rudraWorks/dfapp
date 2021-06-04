from django.http import HttpRequest 
from django.shortcuts import render 
import pyautogui

def home(request):
    return render(request,'home.html')

def form(request):
    res=request.GET.get('name','not found')
    params={'name':res}
    return render(request,'form.html',params)