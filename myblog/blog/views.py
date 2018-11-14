from django.shortcuts import render
from django.http import HttpResponse

def index(response):
    return HttpResponse('欢迎来到我的博客')

# Create your views here.
