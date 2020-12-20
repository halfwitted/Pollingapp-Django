from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

arr = ['Java','Python','C++','C#','C','GO Lang','Visual Basic','R','Ruby','PHP','DotNet','JavaScript','Kotlin','Swift','Assembly language','MATLAB','SQL']
globalcnt = dict()

# Create your views here.
def index(request):
    mydict = {
        "arr" : arr
    }
    return render(request,"index.html",context=mydict)

def getquery(request):
    q = request.POST['languages']
    if q in globalcnt:
        globalcnt[q]=globalcnt[q]+1
    else:
        globalcnt[q]=1

    mydict = {
        "arr" : arr,
        "globalcnt" : globalcnt
    }
    return render(request,'index.html',context=mydict)

def sortres(request):
    global globalcnt
    globalcnt = dict(sorted(globalcnt.items(),key=lambda x:x[1],reverse=True))
    mydict = {
        "arr" : arr,
        "globalcnt" : globalcnt
    }
    return render(request,'index.html',context=mydict)
