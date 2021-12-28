from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    s ='''<h1>For entertainment</h1> <a href = "https://www.youtube.com/"> Youtube</a><br> 
          <h1>Code with harry</h1> <a href ="https://www.youtube.com/watch?v=eTtRhQPZEc0&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=13">Exercise</a><br>'''
    
    return HttpResponse(s)
    
def about(request):
    return HttpResponse("About me")

def spaceback(request):
    return HttpResponse('''<a href = '/'>back</a>''')

def show(request):
    form  = {"name" :"Dhruvil","mobile":9904130708}
    print(request.POST.get('text','default'))
    return render(request,"index.html",{"form":form})

def analyse(request):
    return render(request,"analyze.html")

def analyze(request):
    djtxt = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','OFF')
    Uppercase = request.POST.get('Uppercase','OFF')
    Remove_newlines = request.POST.get('Remove_newlines','OFF')
    Remove_extraspace = request.POST.get('Remove_extraspace','OFF')
    charcount = request.POST.get('charcount','OFF')
   
    # analyzed = djtxt
    if removepunc == "on":
        
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_`'''
        analyzed = ""
        for char  in djtxt:
            if char not in punctuations:
                analyzed = analyzed+char

        params = {'purpose':'Removed Punctuations','analysed_text':analyzed}
        djtxt =analyzed

    if Uppercase == "on" :
        analyzed = djtxt.upper()
        params = {'purpose':'Upper case','analysed_text':analyzed}
        djtxt =analyzed

    if Remove_newlines =="on":
        analyzed = ""
        for char in djtxt :
            if char != "\n" and char != "\r":
                analyzed = analyzed +char
        params = {'purpose':'Remove New Lines','analysed_text':analyzed}
        djtxt =analyzed
    
    if Remove_extraspace =="on":
        analyzed = ""
        for index,char in enumerate(djtxt):
            if djtxt[index]==" " and djtxt[index+1]== " ":
                pass
            else:
                analyzed = analyzed +char
        params = {'purpose':'Remove Extra Spaces','analysed_text':analyzed}
        djtxt =analyzed

    if charcount == "on":
        analyzed = ""
        for char in djtxt:
            if char != " ":
                analyzed = analyzed +char
                c = len(analyzed)
        params = {'purpose':'Count character','analysed_text':c}
    if ( removepunc != "on" and Uppercase != "on" and Remove_newlines != "on" and Remove_extraspace != "on" and charcount != "on"):
        return HttpResponse("Please select any operation and try again")

            
    return render(request,"result.html",params)


    
