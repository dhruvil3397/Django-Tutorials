from django.shortcuts import render,redirect
from .models import Product, UserProfile
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http.response import JsonResponse


# Create your views here.
def home(request):

    return render(request,'base.html')  


def showform(request):

    return render(request,'home.html')  

def showback(request):
        if request.method == "POST":
           
            user = request.user
            print(user)
            if user is request.user:
 
                category =  request.POST.get('category','default')
                type =  request.POST.get('type','default')    
                brand =  request.POST.get('brand','default')
                model =  request.POST.get('model','default')
                color =  request.POST.get('color','default')
                price =  request.POST.get('price','defaut')
                description =  request.POST.get('message','defaut')
                product = Product(user=user,category=category,type=type,brand=brand,model=model,color=color,price=price,description=description)
                product.save()
                print(product.id)
                product = Product.objects.filter(user=user)
                

                return render(request,'table.html',{'product':product})
        user = request.user
        product = Product.objects.filter(user=user)
        return render(request,'table.html',{'product':product})

# def editdetails(request):
#     allContact = Product.objects.get(id = id)
#     return render(request,'showdetail.html',{'allContact':allContact})


def editdata(request):
    id = request.GET.get("id")
    print(id)
    print('*********')
    account = Product.objects.get(id=id)
    print(account)

    return JsonResponse({'valid':True, 'id':account.id,'category':account.category,'type':account.type,'brand':account.brand,'model':account.model,'color':account.color,'price':account.price,'description':account.description}, status = 200)

def updatedata(request):
    
    # if request.is_ajax and request.method == "GET":
    id1 = request.GET.get('id')
    print(id1)
    category =  request.GET.get('id2')
    type =  request.GET.get('id3')    
    brand =  request.GET.get('id4')
    model =  request.GET.get('id5')
    color =  request.GET.get('id6')
    price =  request.GET.get('id7')
    description =  request.GET.get('id8')

    
    print('////////////////')
    print(category)
    print('////////////////')
    print(type)
    print('////////////////')
    print(brand)
    print('////////////////')
    print(model)
    print('////////////////')
    print(color)
    print('////////////////')
    print(price)
    print('////////////////')
    print(description)
    print('////////////////')

    account = Product.objects.get(id = id1)
    account.category = category
    account.type = type
    account.brand = brand
    account.model = model
    account.color = color
    account.price = price
    account.description = description  
    account.save()

    return JsonResponse({'valid':True}, status = 200)
                
def deletedata(request):
    id = request.GET.get("id")
    print(id)
    print('*********')
    account = Product.objects.get(id = id)
    print(account)
    account.delete()
    
    #allContact = Contact.objects.all()
    return JsonResponse({'valid':True}, status = 200)

def viewdata(request):
    a = UserProfile.objects.values()
    print(a)
    id = request.GET.get("id")
    print(id)
    print('*********')
    account = Product.objects.get(id = id)
    # stu = StudentSerializer(account)
    # print(stu.data)3
    print(account.price)
    print(account.description)
    

    return JsonResponse({'valid':True, 'category':account.category,'type':account.type,'brand':account.brand,'model':account.model,'color':account.color,'price':account.price,'description':account.description}, status = 200)

    #return render(request,'view.html',{'account':account})

def signup(request):

    if request.method == "POST":
        username =  request.POST.get('username','default')
        firstname =  request.POST.get('firstname','default')    
        lastname =  request.POST.get('lastname','default')
        email =  request.POST.get('email','default')
        password =  request.POST.get('password','default')
        address = request.POST.get('address','default')
        phone = request.POST.get('phone','default')

        myuser = User.objects.create_user(username,email,password)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.save()
        # store the data in UserProfile
        profile = UserProfile()
        profile.user = myuser
        profile.address = address
        profile.phone = phone
        profile.save()
 


        messages.success(request,"Your account has been successfully created")
        return redirect('/')
    else :    
        return HttpResponse('404 - Not Found')

def loginhandle(request):
    if request.method  == "POST" :
        loginusername = request.POST.get('username','default')     
        loginpassword = request.POST.get('password','default')
        user = User.objects.get(username = loginusername)
        print(user)
       
        print('********************')
        profile = UserProfile.objects.get(user=user)
        print(profile.active)
        print('////')
        if profile.active == True:
            user = authenticate(username = loginusername,password = loginpassword)
            print(user)
            if user is not None :
                login(request,user)
                messages.success(request,"You have successfully logged in")
                product = Product.objects.filter(user = user)
                print(product)
                return render(request,'table.html',{'product':product})
            else :
                messages.error(request,"Invalid Credentials,Please enter valid details ")
                return redirect('/')
        messages.error(request,"You might not be used your account for a long time")
        return redirect('/')
   
    return HttpResponse('404 - Not Found')


def logouthandle(request):
    logout(request)
    messages.success(request,"You have successfully logged out")
    return redirect('/')
    

