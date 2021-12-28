from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact
from math import ceil

# Create your views here.   
def index(request): 
    allProds = []
    catprods = Product.objects.values('category')
    print(catprods)

    cats = {item['category'] for item in catprods}
    print(cats)

    for cat in cats:
       prod = Product.objects.filter(category = cat)
       n = len(prod)
       nSlides = n//4 + ceil((n/4)-(n//4))
       allProds.append([prod,range(1,nSlides),nSlides])
    print(allProds)

    params = {'allProds':allProds}
    return render(request,"shop/index.html", params)
    


def about(request): 
    return render(request,'shop/about.html')
def contact(request):
    name =  request.POST.get('name','default')
    email =  request.POST.get('email','default')
    phone =  request.POST.get('phone','default')
    message =  request.POST.get('message','default')
    # params = {'name':name,'email':email,'phone':phone,'message':message}
    contact = Contact(name = name,email = email,phone = phone,message = message)
    contact.save()
    return render(request,'shop/contact.html')


def tracker(request):
    return render(request,'shop/tracker.html')
def search(request):
    return HttpResponse("This is an e-commerce website")
def productview(request,myid):
    # fetch the products using the id
    product = Product.objects.filter(id = myid)
    print(product)
    return render(request,'shop/products.html',{'product':product[0]})
def search(request):
    return HttpResponse("This is an e-commerce website")