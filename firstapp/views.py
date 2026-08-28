from django.shortcuts import render
from .models import appvarity

# Create your views here.
def all_app(request):
    apps=appvarity.objects.all
    return render(request,'firstapp/all_app.html',{'apps':apps})
#def app_details(request,app_id):
    #app= get _object_or_404(appvarity,pk=app_id)
    #return render(request,'app/app_details.html',{'app':app})
def app_store_view(request):
    return render(request,'firstapp/app_store.html')