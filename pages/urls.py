from django.urls import path
from . import views

urlpatterns = [

    # ── SEO ───────────────────────────────────────────────────────────────────
    path('sitemap.xml', views.sitemap_view, name='sitemap'),
    path('robots.txt',  views.robots_txt_view, name='robots-txt'),

    path('', views.home, name='home'),
    path('home.html', views.home, name='home'),

    path('about.html', views.about, name='about'),
    path('contact.html', views.contact, name='contact'),
    path('projects.html', views.projects, name='projects'),

    path('home-lift.html', views.homelift, name='home-lift'),
    path('passenger-lift.html', views.passengerlift, name='passenger-lift'),
    path('hospital-lift.html', views.hospitallift, name='hospital-lift'),
    path('capsule-lift.html', views.capsulelift, name='capsule-lift'),
    path('goods-lift.html', views.goodslift, name='goods-lift'),
    path('car-lift.html', views.carlift, name='car-lift'),
    path('chair.html', views.chairlift, name='chair-lift'),

 
    path('home-hydraulic-lift.html', views.home_hydraulic_lift, name='home-hydraulic-lift'),
    path('home-belt-drive-lift.html', views.home_belt_drive_lift, name='home-belt-drive-lift'),
    path('passenger-geared-lift.html', views.passenger_geared_lift, name='passenger-geared-lift'),
    path('passenger-gearless-lift.html', views.passenger_gearless_lift, name='passenger-gearless-lift'),
    path('geared-hospital-lift.html', views.geared_hospital_lift, name='geared-hospital-lift'),
    path('gearless-hospital-lift.html', views.gearless_hospital_lift, name='gearless-hospital-lift'),
    path('manual-goods-lift.html', views.manual_goods_lift, name='manual-goods-lift'),
    path('automatic-goods-lift.html', views.automatic_goods_lift, name='automatic-goods-lift'),
    path('manual-car-lift.html', views.manual_car_lift, name='manual-car-lift'),
    path('automatic-car-lift.html', views.automatic_car_lift, name='automatic-car-lift'),
    path('double-stacker-parking-lift.html', views.double_stacker_parking_lift, name='duble-stacker-parking-lift'),

    path('clients.html', views.clients, name='clients'),
    path('blog.html', views.blog, name='blog'),

    path('save-lead/', views.save_lead, name='save-lead'),

    # ADMIN PAGES
  path('dashboard/dashboard.html', views.dashboard, name='dashboard'),

path('dashboard/admin-login.html', views.admin_login, name='admin-login'),

]