
from django.urls import path, include

from movieapp import views
app_name= 'movieapp'

urlpatterns = [

    path('',views.index,name='index'),
    path('movie/<int:movies_id>/',views.details,name='details'),
    path('add/',views.add,name='add'),
    path('update/<int:id>/',views.update,name= 'update'),
    path('delete/<int:id>/',views.delete,name= 'delete')
]
