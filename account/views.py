from django.shortcuts import render

# Create your views here.
def registarion(request):

    return render(request,'reg.html')
def login(request):
    return render(request,'log.html')