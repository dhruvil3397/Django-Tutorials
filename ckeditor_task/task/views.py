from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse
from django.http.response import JsonResponse

# Create your views here.
def home(request):
    if request.method == "POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        message = request.POST.get('message','')

        if len(name)<1 or len(email)<5 or len(phone)<10 or len(message)<2:
            return HttpResponse("Sorry,Please fill the details")
        

        contact = Contact(name = name,email=email,phone = phone,message = message)
        contact.save()
      
        params = {'name':name,'email':email,'phone':phone,'message':message}
        # redirect contact information to another page
        #con = Contact.objects.filter(name = contact.name) 
      
        return render(request,'home.html',{'params':params})
        
    return render(request,'home.html')

def show(request):
    allContact = Contact.objects.all()
    print(allContact)
    
    return render(request,'allContact.html',{'allContact':allContact})

def showdetails(request,id):
    allContact = Contact.objects.filter(id = id)
    return render(request,'showdetail.html',{'allContact':allContact})

def updatedetails(request,id):
    if request.method == "POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        message = request.POST.get('message','')
        account = Contact.objects.get(id = id)
        account.name = name
        account.email = email
        account.phone = phone
        account.message = message
        account.save()
      
   
    return render(request,'home.html')


def deletedata(request):
    id = request.GET.get("id")
    account = Contact.objects.get(id = id)
    print(account)
    account.delete()
    
    #allContact = Contact.objects.all()
    return JsonResponse({'valid':True}, status = 200)
    #return render(request,'allContact.html',{'allContact':allContact})

