#I have created this file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("hello")

def removepunc(request):
    return HttpResponse("removepunc")

def capitalize(request):
    return HttpResponse("capitalized")

def newlineremove(request):
    return HttpResponse("newlineremoved")

def spaceremove(request):
    return HttpResponse("space removed")

def charcount(request):
    return HttpResponse("charcounted")



