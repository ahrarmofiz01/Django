from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    #return HttpResponse("hello,world,this is your home page")
    return render(request,'website/index.html')
def dashbord(request):
    return HttpResponse(" welcome this is your dashbord site")
def about(request):
    return HttpResponse("hello,world,thsi is about page")
def contact(request):
    return HttpResponse("hello,world,this is your contavt page")