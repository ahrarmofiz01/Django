from django.shortcuts import render
from .models import appvarity

# Create your views here.
def all_app(request):
    apps=appvarity.objects.all
    return render(request,'firstapp/all_app.html',{'apps':apps})
