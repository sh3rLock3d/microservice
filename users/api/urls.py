from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dr/signin', views.dr_signin, name='dr_signin'),
    path('dr/login', views.dr_login, name='dr_login'),
    path('dr/get_profile', views.dr_get_profile, name='dr_get_profile'),

    path('p/signin', views.p_signin, name='p_signin'),
    path('p/login', views.p_login, name='p_login'),
    path('p/get_profile', views.p_get_profile, name='p_get_profile'),
    
    path('a/login', views.admin_login, name='admin_login'),
    path('a/getProfile', views.admin_getProfile, name='admin_getProfile'),
    
    
]