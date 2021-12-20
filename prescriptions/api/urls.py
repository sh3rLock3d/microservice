from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dr/addPrescription', views.dr_addPrescription, name='dr_addPrescription'),
    path('p/listpres', views.p_listpres, name='p_listpres'),
    path('a/getstatistics', views.admin_getstatistics, name='admin_getstatistics'),
]