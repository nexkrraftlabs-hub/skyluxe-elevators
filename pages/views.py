from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.conf import settings
from django.template.loader import render_to_string
from datetime import date
from .models import Lead


# Create your views here.
def dashboard(request):
    return render(request, 'adminpanel/dashboard.html')


def admin_login(request):
    return render(request, 'adminpanel/admin-login.html')
def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

def projects(request):
    return render(request, 'pages/projects.html')


def homelift(request):
    return render(request, 'pages/home-lift.html')

def passengerlift(request):
    return render(request, 'pages/passenger-lift.html')

def hospitallift(request):
    return render(request, 'pages/hospital-lift.html')

def capsulelift(request):
    return render(request, 'pages/capsule-lift.html')

def goodslift(request):
    return render(request, 'pages/goods-lift.html')

def carlift(request):
    return render(request, 'pages/car-lift.html')

def chairlift(request):
    return render(request, 'pages/chair.html')

# New Variation Views (8 files)
def home_hydraulic_lift(request):
    return render(request, 'pages/home-hydraulic-lift.html')


def home_belt_drive_lift(request):
    return render(request, 'pages/home-belt-drive-lift.html')


def passenger_geared_lift(request):
    return render(request, 'pages/passenger-geared-lift.html')

def passenger_gearless_lift(request):
    return render(request, 'pages/passenger-gearless-lift.html')

def geared_hospital_lift(request):
    return render(request, 'pages/geared-hospital-lift.html')

def gearless_hospital_lift(request):
    return render(request, 'pages/gearless-hospital-lift.html')

def manual_goods_lift(request):
    return render(request, 'pages/manual-goods-lift.html')

def automatic_goods_lift(request):
    return render(request, 'pages/automatic-goods-lift.html')

def manual_car_lift(request):
    return render(request, 'pages/manual-car-lift.html')

def automatic_car_lift(request):
    return render(request, 'pages/automatic-car-lift.html')

def double_stacker_parking_lift(request):
    return render(request, 'pages/double-stacker-parking-lift.html')

def save_lead(request):
    if request.method == 'POST':
        Lead.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            city=request.POST.get('city'),
            message=request.POST.get('message')
        )
        messages.success(request, 'Your query has been sent successfully!')
        # Redirect back to the page that submitted the form
        referer = request.META.get('HTTP_REFERER', '/')
        return redirect(referer)
    return redirect('/')

def clients(request):
    return render(request, 'pages/clients.html')

def blog(request):
    return render(request, 'pages/blog.html')


# ─── SEO VIEWS ────────────────────────────────────────────────────────────────

def sitemap_view(request):
    """Serve dynamic XML sitemap for Google Search Console."""
    site_url = getattr(settings, 'SITE_URL', 'https://www.skyluxeelevators.com')
    context = {
        'site_url': site_url.rstrip('/'),
        'today': date.today().isoformat(),
    }
    content = render_to_string('pages/sitemap.xml', context)
    return HttpResponse(content, content_type='application/xml; charset=utf-8')


def robots_txt_view(request):
    """Serve robots.txt with correct sitemap URL."""
    site_url = getattr(settings, 'SITE_URL', 'https://www.skyluxeelevators.com')
    context = {'site_url': site_url.rstrip('/')}
    content = render_to_string('pages/robots.txt', context)
    return HttpResponse(content, content_type='text/plain; charset=utf-8')
