#I have created this file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # print(request.GET.get('text'))
    return render(request, 'index.html')
    # return HttpResponse("hello")

def analyze(request):
    djtext = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    print(removepunc)
    print(djtext)   
    return HttpResponse("removepunc")
# 
# def capitalize(request):
#     return HttpResponse("capitalized")

# def newlineremove(request):
#     return HttpResponse("newlineremoved")

# def spaceremove(request):
#     return HttpResponse("space removed")

# def charcount(request):
#     return HttpResponse("charcounted")



