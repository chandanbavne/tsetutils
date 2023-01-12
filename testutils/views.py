from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request,'index.html')

# def removepunc(request):
#     djtext=(request.GET.get('text','default'))
#     print(djtext)
#     return HttpResponse("remove punc")   

def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','default')
    fullcaps=request.POST.get('fullcaps','off')
    ExtraSpaces=request.POST.get('ExtraSpaces','off')
    charcount=request.POST.get('charcount','off')
    print(removepunc)
    if removepunc=="on":
        punctuations=''' !@#$%"",.{}[]*&'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char


        params={"purpose":'remove punctions','analyze_text':analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',params)        
    if fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={"purpose":"change to Upper","analyze_text":analyzed} 
        djtext=analyzed
        #return render(request,'analyze.html',params)    
    if ExtraSpaces=='on':
        analyzed=""
        for index,char in enumerate(djtext):
            if (djtext[index]==" " and djtext[index+1]==" "):
                pass
            else:
                analyzed=analyzed+char
        params={"purpose":"remove extraspace","analyze_text":analyzed}    
        djtext=analyzed
        #return render(request,'analyze.html',params)         
    if charcount=="on":
        analyzed="no of character count is:"
        count=0
        for char in djtext:
            count+=1
        analyzed+=str(count)    
        params={"purpose":"remove extraspace","analyze_text":analyzed}    
        djtext=analyzed
    if(removepunc!="on"and fullcaps!="on" and ExtraSpaces!='on' and charcount!="on"):
        return HttpResponse("please select the checkbox")

    return render(request,'analyze.html',params)  
    

def ex1(request):
    s=''' <h1>Navigation Bar<h1><br><a href="https://www.google.com/">Google</a><br>
        <a href="https://www.facebook.com/">facebook</a>
     '''  
    return HttpResponse(s) 