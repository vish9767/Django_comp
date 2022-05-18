from django.shortcuts import render
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
from . import models
# Create your views here.
def home(request):
    pro=models.complaint.objects.all()

    hom=[1,2,3]
    return render(request,'index.html',{'hom':pro})
def comp(request):
    if(request.method=='POST'):
        compl=models.complaint()
        compl.user_name=request.POST.get('u1')
        compl.email=request.POST.get('e1')
        compl.company_name=request.POST.get('c1')
        compl.mobile_name=request.POST.get('m1')
        compl.problem=request.POST.get('p1')
        compl.pic=request.FILES['im2']
        compl.save()
        return render(request,'sub.html')
        #compl=User.objects.create_user(name=name,email=email,company=comp,mobile=mob,problem=pro,picture=pic)
        #compl.save()
        #print("data saved")
        #return HttpResponse(request,"data")
    else:
        return render(request,'com.html')
def hom(request):
    return render(request,'index.html')
def mob(request):
    sli=models.slid.objects.all()
    mob=models.dev.objects.all()
    return render(request,'mob.html',{'side':sli,'mob':mob})
