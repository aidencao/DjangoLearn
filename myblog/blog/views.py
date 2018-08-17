from django.shortcuts import render
from django.http import HttpResponse
from . import models



def index(request):
    article = models.Article.objects.get(id=1)
    print(article.content)
    return render(request,'blog/index.html',{'article':article})

# Create your views here.
