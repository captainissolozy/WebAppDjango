from django.urls import path
from django.views.generic import TemplateView
from . import views


app_name = 'home'
urlpatterns = [
    path('', TemplateView.as_view(template_name='login.html'), name='home'),
    path('check_auth/', views.check_auth, name='check'),
]