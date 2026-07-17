# adminpanel/urls.py

from django.urls import path

from . import views

app_name = 'adminpanel'
urlpatterns = [

    # LOGIN

    path(
        'admin-login.html',
        views.admin_login,
        name='admin_login'
    ),

    # DASHBOARD

    path(
        '',
        views.dashboard,
        name='dashboard'
    ),

    path(
        'dashboard.html',
        views.dashboard,
        name='dashboard'
    ),

    # LEADS

    path('leads/', views.leads, name='leads'), 


    # PROFILE

    path(
        'profile.html',
        views.profile,
        name='profile'
    ),

    # LOGOUT

    path(
        'logout/',
        views.admin_logout,
        name='logout'
    ),

]