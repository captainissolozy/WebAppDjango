from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'customer'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_co/', views.add_co, name='add_co'),
    path('add_cp/', views.add_cp, name='add_cp'),
    path('add_co/add_customerO/', views.add_customerO, name='add_add_co'),
    path('add_cp/add_customerP/', views.add_customerP, name='add_add_cp'),
]
