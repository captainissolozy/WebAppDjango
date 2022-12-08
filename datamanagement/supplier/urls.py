from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'supplier'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_so/', views.add_so, name='add_so'),
    path('add_sp/', views.add_sp, name='add_sp'),
    path('add_so/add_supplierO/', views.add_supplierO, name='add_add_so'),
    path('add_sp/add_supplierP/', views.add_supplierP, name='add_add_sp'),
]
