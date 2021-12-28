from django.shortcuts import render
from django.http import HttpResponse
from .forms import Studentform
from .models import Student
from .resourses import PersonResource
from django.contrib import messages
from tablib  import Dataset




# Create your views here.
def Showdetails(request):
    if request.method =="POST":
        form = Studentform(request.POST)
        if form.is_valid():
            nm = form.cleaned_data["name"]
            em = form.cleaned_data["email"]
            mo = form.cleaned_data["mobile"]
            co = form.cleaned_data["course"]
            
            form.save()
            print(nm)
            print(em) 
            print(mo)
            print(co)  
    form = Studentform()
    return render(request,"practical/form.html",{"form":form})

def export(request):
    person_resource = PersonResource()
    print(person_resource)
    
    dataset =person_resource.export()
    print(dataset)
    response = HttpResponse(dataset.xls,content_type = 'application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment ; filename = "person.xls"'
    return response

    
def uploadfiles(request):
    if request.method =="POST": 
        
        dataset = Dataset()
        print(dataset)
        new_person =request.FILES['myfile']
        print(new_person)

        if not new_person.name.endswith('xlsx'):
            messages.info(request,'wrong format')
            return render(request,"practical/form1.html")

        imported_data = dataset.load(new_person.read(),format='xlsx')
        print(imported_data)
        for data in imported_data:
            value = Student(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4]
                )
            value.save()
    return render(request,"practical/form1.html")