from django.urls import path
from myapp import views
     



urlpatterns = [
    path('', views.add, name='add'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update<int:id>/',views.update,name='update'),
    
]
