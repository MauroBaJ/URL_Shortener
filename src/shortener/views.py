from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

def FRV(request, *args, **kwargs): #Function Redirect View
    print(args)
    print(kwargs)
    return HttpResponse("Hello")

class CRV(View): #Class Redirect View
    def get(self, request, *args, **kwargs):
        print(args)
        print(kwargs)
        return HttpResponse("Hello again")