from django.shortcuts import redirect, render
from django.http import HttpResponse
from blog.models import Post
from django.contrib.auth import authenticate,login,logout
from blog.models import Post
from .models import Contact
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    return render(request,'home/home.html')

def about(request):
   # messages.success(request, 'This is about')
    return render(request,'home/about.html')

def contact(request):
    
    if request.method == "POST":
        name =  request.POST.get('name','default')
        email =  request.POST.get('email','default')    
        phone =  request.POST.get('phone','default')
        message =  request.POST.get('message','default')

        if len(name)<2 or len(email)<5 or len(phone)<10 or len(message)<4:
            messages.error(request,"Please fill the form correctly")
        else:
       
            # params = {'name':name,'email':email,'phone':phone,'message':message}
            contact = Contact(name = name,email = email,phone = phone,message = message)
            contact.save()
            messages.success(request,"Your message has been successfully sent")
       
    return render(request,'home/contact.html')



def search(request):
    query = request.GET.get('search')
    if len(query) ==0 or len(query) <3 or len(query)>50 :
        allPost  = []
    else :
        allPostTitle = Post.objects.filter(title__icontains = query) 
        allPostAuthor= Post.objects.filter(author__icontains=query)
        allPostContent =Post.objects.filter(content__icontains=query)
        allPost=  allPostTitle.union(allPostContent, allPostAuthor)
    if len(allPost) == 0:
        messages.warning(request, "No search results found. Please refine your query.")

    print(allPost)
    params = {'allPost':allPost,'query':query}
    print(params)
  
    
    return render(request,"home/search.html", params)


def signup(request):

    if request.method == "POST":
        username =  request.POST.get('username','default')
        firstname =  request.POST.get('firstname','default')    
        lastname =  request.POST.get('lastname','default')
        email =  request.POST.get('email','default')
        password =  request.POST.get('password','default')
        confirmpassword =  request.POST.get('confirmpassword','default')


        # check for errorneous inputs
        # username shold be under 10 characters
        if len(username)>10:
            messages.error(request,"Username must be under 10 characters")
            return redirect('/home/')
        
        # username should be alphanumeric
        elif not username.isalnum():
            messages.error(request,"Username shold only contain letters and numbers")
            return redirect('/home/')
        # passwords should match
        elif password != confirmpassword:
            messages.error(request,"Passwords do not match")
            return redirect('/home/')   

        
        # create the user 
        myuser = User.objects.create_user(username,email,password)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.save()
        messages.success(request,"Your account has been successfully created")
        return redirect('/home/')
    else :    
        return HttpResponse('404 - Not Found')

def loginhandle(request):
    if request.method  == "POST":
        loginusername = request.POST.get('username','default')     
        loginpassword = request.POST.get('password','default')

        user = authenticate(username = loginusername,password = loginpassword)
        print(user)
        if user is not None:
            login(request,user)
            messages.success(request,"You have successfully logged in")
            return redirect('/home/')
        else :
            messages.error(request,"Invalid Credentials,Please enter valid details")
            return redirect('/home/')
    return HttpResponse('404 - Not Found')


def logouthandle(request):
    logout(request)
    messages.success(request,"You have successfully logged out")
    return redirect('/home/')
    

    

    

