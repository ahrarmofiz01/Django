from django.shortcuts import render

# Create your views here.
def all_app(request):
    return render(request,'firstapp/all_app.html')
