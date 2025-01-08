from django.urls import path
from .import views

urlpatterns = [
    path('',views.home), 
    path('add',views.addemployee,name='addemp'), 
    path('dis',views.display),   
    path('del',views.delemployee),  
    # path('delemp/<int:eid>',views.deleteemp), 
    path('update',views.updatename)

]
#http://127.0.0.1:8000/delemp/2

# CRUD