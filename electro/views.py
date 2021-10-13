from django.shortcuts import render
from.forms import *
from .models import *
from . import models

from django.http import HttpResponse , HttpResponseRedirect
# Create your views here.

def home(request):
    product = models.Product.objects.all()
    return render(request,'store2.html',{'product':product})

def register(request):
    if(request.method == 'GET'):
        f=Userform()
        return render(request, 'registration.html', {'form': f})
    else:
        f = Userform(request.POST)
        if(f.is_valid()):
            fname = request.POST['name']
            femail = request.POST['email']
            fpassword = request.POST['password']
            faddress = request.POST['address']
            ftelephone = request.POST['phonenumber']
            try:
                User.objects.create(name=fname,email=femail,password=fpassword,address=faddress,telephone=ftelephone)
                print ('User added')
                return  HttpResponseRedirect("/login/")
            except:
                return render(request, 'registration.html', {'form': f,'wrong':"* this Email already registered"})

def login(request):
    if (request.method == 'GET'):
        f = loginUser()
    else:
        f = loginUser(request.POST)
        if(f.is_valid()):
            femail = request.POST['email']
            fpassword = request.POST['password']
            try:
              result = User.objects.get(email=femail,password=fpassword)
              return HttpResponse("exist")
            except:
                return render(request, 'login.html', {'form': f,'wrong':"*wrong Email or Password"})
    return render(request,'login.html',{'form':f})

def filter(request):
    if (request.method == 'POST'):
        price_min=float(request.POST['price-min'])
        price_max=float(request.POST['price-max'])

        categoires=[]
        if 'Laptops' in request.POST:
            categoires.append('Laptops')
        if 'Smartphones' in request.POST:
            categoires.append('Smartphones')
        if 'Cameras' in request.POST:
            categoires.append('Cameras')
        if 'Accessories' in request.POST:
            categoires.append('Accessories')

        if len(categoires) == 0:
            product = Product.objects.filter(price__range=(price_min,price_max))
        else:
            product = Product.objects.filter(price__range=(price_min,price_max),category__in=categoires)
        return render(request, 'store2.html', {'product': product})


def details(request,product_id):
    prd=models.Product.objects.get(id=product_id)
    return render(request,'product.html',{'pd':prd})

'''
            print(type(request.POST['cat1']))
            print(request.POST['cat1'])
            return HttpResponse('its working!')
        return HttpResponse('its working! no inputs')
'''


