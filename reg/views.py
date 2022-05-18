from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.
def login(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['password']
        print("hi1")
        user = auth.authenticate(username=user_name, password=password)
        print("h2")
        if user is not None:
            print("h3")
            auth.login(request, user)
            return redirect("com/home")
        else:
            messages.info(request, "user name or password is wrong")
            return redirect('/')
    else:
        return render(request, "log.html")
def newu(request):
    if(request.method=="POST"):
        first_name=request.POST['1name']
        last_name=request.POST['2name']
        email=request.POST['email']
        username=request.POST['ui']
        password1=request.POST['p1']
        password2=request.POST['p2']
        if(password1==password2):
            if User.objects.filter(username=username).exists():
                messages.info(request,'username is already taken')
                return redirect('newu')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email is already taken ')
                return redirect('newu')
            else:
                user=User.objects.create_user(username=username,email=email,password=password1,first_name=first_name,last_name=last_name)
                user.save();
        else:
            messages.info(request,'password is not matching')
            return redirect('newu')
        messages.info(request,"Registration Succuesful")
        return redirect('/')
    else:
        return render(request,'new.html')