from django.db.models import query
from django.shortcuts import render
from django.http import HttpResponse, response
from .models import Product,Contact,Orders,OrderUpdate
from math import ceil
import json
from django.views.decorators.csrf import csrf_exempt
from .PayTm import Checksum
MERCHANT_KEY = 'bKMfNxPPf_QdZppa'

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

def searchmatch(query,item):
    '''return True only if query matches the item'''
    if query in item.category.lower() or query in item.type.lower() or query in item.brand.lower() or query in item.model.lower():
        return True
    else :
        False

def search(request):
    query = request.GET.get('search')
    print(query)
    allProds = []
    catprods = Product.objects.values('category')
    print(catprods)
   

    cats = {item['category'] for item in catprods}
    print(cats)

    for cat in cats:
        prodtemp = Product.objects.filter(category = cat)
        prod = [item for item in prodtemp if searchmatch(query,item)]
        print('______________________________')
        print(prod)
        print('______________________________')
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4)) 
        if len(prod) != 0:
            allProds.append([prod,range(1,nSlides),nSlides])
      
    print(allProds)

    params = {'allProds':allProds,"msg":""}
    if len(allProds)==0 or len(query)<2:
        params={'msg':"Please make sure to enter relevant search query"}

    return render(request,"shop/search.html", params)
    


def about(request): 
    return render(request,'shop/about.html')
def contact(request):
    thank = False
    if request.method == "POST":
        name =  request.POST.get('name','default')
        email =  request.POST.get('email','default')
        phone =  request.POST.get('phone','default')
        message =  request.POST.get('message','default')
        # params = {'name':name,'email':email,'phone':phone,'message':message}
        contact = Contact(name = name,email = email,phone = phone,message = message)
        contact.save()
        thank = True
    return render(request,'shop/contact.html',{'thank':thank})
    

def tracker(request):
    if request.method == "POST":
        order_id = request.POST.get('order_id','')
        email =  request.POST.get('email','')
        try:
            order = Orders.objects.filter(order_id = order_id,email = email)
            if len(order) >0:
                update = OrderUpdate.objects.filter(order_id = order_id)
                updates = []
                for item in update:
                    updates.append({'text':item.update_desc, 'time': item.timestamp})
                    response = json.dumps({"status": "success","updates": updates,"items_json" : order[0].items_json}, default = str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"No Items"}')
        except: 
            return HttpResponse('{"status":"error"}')

    return render(request,'shop/tracker.html')



def productview(request,myid):
    # fetch the products using the id
    product = Product.objects.filter(id = myid)
    print(product)
    return render(request,'shop/products.html',{'product':product[0]})

def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('items_json','')
        amount = request.POST.get('amount','')
        name =  request.POST.get('name','')
        email =  request.POST.get('email','')
        address =  request.POST.get('address1','') + " " + request.POST.get('address2','')
        phone =  request.POST.get('phone','')
        city =  request.POST.get('city','')
        state =  request.POST.get('state','')
        zip_code =  request.POST.get('zip_code','')
        order = Orders(items_json = items_json,amount = amount,name =name,email = email,address =address,phone= phone,city = city, state= state,zip_code= zip_code)
        order.save()
        thank = True
        id = order.order_id
        update = OrderUpdate(order_id=id,update_desc= "The Order has been placed")
        update.save()
      

        return render(request,'shop/checkout.html',{'thank':thank,'id':id})
        # Request paytm to transfer the amount to your account after paymment
     
        param_dict = {

                'MID': 'DIY12386817555501617',
                'ORDER_ID': str(order.order_id),
                'TXN_AMOUNT': str(amount),
                'CUST_ID': 'dhruvil@logicrays.com',   
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': 'WEBSTAGING',
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL':'http://127.0.0.1:8005/shop/handlerequest/',

        }
       
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request, 'shop/paytm.html', {'param_dict': param_dict})
    

    return render(request,'shop/checkout.html')

@csrf_exempt
def handlerequest(request):
    
    # Paytm will send you post request here
    form = request.POST
    
    response_dict = {}  
    for i in form.keys():
        response_dict[i]= form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]
    verify = Checksum.verify_checksum(response_dict,MERCHANT_KEY,checksum)

    if verify :
        if response_dict["RESPCODE"] == '01':
            print('Order Successful')
        else:
            print('Order was not Successful because' + response_dict['RESPMSG'])
    return render(request,'shop/paymentstatus.html',{'response':response_dict})

    #return HttpResponse('done')
    