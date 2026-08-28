from django.urls import path
from.import views

#localhost:800/app
urlpatterns = [
    path('',views.all_app , name='all_app'),
    path('app_store/',views.app_store_view,name='app_store')
    
   
]
