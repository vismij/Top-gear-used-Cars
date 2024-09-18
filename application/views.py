from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import reg

from.models import login
def home(request):
    return render(request,'front page.html')
def register(request):
    if request.method=='POST':
        a=request.POST['n1']
        b=request.POST['n2']
        c=request.POST['n3']
        d=request.POST['n4']
        e=request.POST['n5']
        f=request.POST['n6']
        data=reg.objects.create(name=a,age=b,phone=c,email=d,user=e,password=f)
        data.save()
    return render(request,'register.html')
    return HttpResponse("created")

def display(request):
    if request.method=='GET':
        data=reg.objects.all()
    return render(request,'display.html',{'r':data})

def addlogin(request):
    if request.method=='POST':
        u=request.POST['username']
        p=request.POST['password']
        user=reg.objects.all().filter(user=u,password=p)
        if user:
            return render(request,'VJ CARS.html')
        else:
            return render(request, 'login.html')
        #     return HttpResponse("User name or password not found.")
    else:
        return render(request,'login.html')

def logout(request):
    if 'user' in request.session:
        request.session.flush()
    return redirect(home)
def news(request):
    return render(request,'news.html')
def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')

def maruti(request):
    return render(request,'maruti.html')
def alto(request):
    return render(request,'alto.html')
def ritz(request):
    return render(request,'ritz.html')
def swift(request):
    return render(request,'swift.html')
def wagnor(request):
    return render(request,'wagnor.html')

def toyota(request):
    return render(request,'toyota.html')
def liva(request):
    return render(request,'liva.html')
def innova(request):
    return render(request,'innova.html')
def fortuner(request):
    return render(request,'fortuner.html')
def landcruiser(request):
    return render(request,'landcruiser.html')

def honda(request):
    return render(request,'honda.html')
def hondaamaze(request):
    return render(request,'hondaamaze.html')
def hondabrio(request):
    return render(request,'hondabrio.html')
def hondacity(request):
    return render(request,'hondacity.html')
def hondajazz(request):
    return render(request,'hondajazz.html')

def hyundai(request):
    return render(request,'hyundai.html')
def creta(request):
    return render(request,'creta.html')
def i10(request):
    return render(request,'i10.html')
def i20(request):
    return render(request,'i20.html')
def venue(request):
    return render(request,'venue.html')




