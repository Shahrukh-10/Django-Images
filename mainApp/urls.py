from django.urls import path , include
from . import views
urlpatterns = [
    path('',views.index,name='Home'),
    path('category/<int:cid>/',views.category,name='Cat'),
]