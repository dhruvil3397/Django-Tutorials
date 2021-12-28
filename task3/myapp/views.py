from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from .resources import StudentResource
from tablib  import Dataset


# Create your views here.
def home(request):
    return render(request,'base.html')


def uploadfiles(request):
    if request.method =="POST": 
        
        dataset = Dataset()
        print(dataset)
        new_person =request.FILES['myfile']
        print(new_person)

        if not new_person.name.endswith('xls'):
          
            return render(request,"base.html")

        imported_data = dataset.load(new_person.read(),format='xls')
        print(imported_data)
        for data in imported_data:
            id = data[0]
            name = data[1]
            email = data[2]
            num1 = data[3]
            num2 = data[3]*2
            
            print(id,name,email,num1,num2)
            value = Student(id,name,email,num1,num2)
            value.save()
        
    return render(request,"import.html")