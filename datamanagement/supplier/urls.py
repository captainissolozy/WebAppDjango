from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'supplier'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_so/', views.add_so, name='add_so'),
    path('add_sp/', views.add_sp, name='add_sp'),
    path('add_so/add_supplierO/', views.add_supplierO, name='add_add_so'),
    path('add_sp/add_supplierP/', views.add_supplierP, name='add_add_sp'),
    path('inside_per/<str:email>', views.inside_per, name='inside_p'),
    path('inside_org/<str:name>', views.inside_org, name='inside_o'),
    path('test/', views.add_dp, name='test')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


