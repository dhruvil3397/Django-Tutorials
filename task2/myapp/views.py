import xlwt
from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
import csv
from django.core import serializers
import json

def home(request):
    return render(request,'base.html')

    
def export_xls(request):
    if request.method == 'POST':
        # Get selected option from form
        file_format = request.POST['file-format']

        if file_format == 'XLS (Excel)':
            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="employee.xls"'

            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('Employee')

            # Sheet header, first row
            row_num = 0

            font_style = xlwt.XFStyle()
            font_style.font.bold = True

            columns = ['First name', 'Last name', 'Email address','Day started','Location' ]

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()

            rows = Employee.objects.all().values_list('first_name', 'last_name', 'email','day_started','location')
            for row in rows:
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)

            wb.save(response)
            return response
        
        elif file_format == 'JSON':
            data = serializers.serialize("json", Employee.objects.all())
            js = json.dumps(data)
            with open("record.json","w") as file:
                file.write(js)

            return HttpResponse("record.json")


        elif file_format == 'CSV':
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="exported_data.csv"'
            writer = csv.writer(response)
            writer.writerow(['First name', 'Last name', 'Email address','Day started','Location' ])

            employees = Employee.objects.all().values_list('first_name', 'last_name', 'email','day_started','location')
            for employee in employees:
                writer.writerow(employee)

            return response
          

    return render(request, 'export.html')

