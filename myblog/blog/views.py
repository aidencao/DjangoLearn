from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html',{'Hello':'Hello,aaaBlog!'})

# Create your views here.
