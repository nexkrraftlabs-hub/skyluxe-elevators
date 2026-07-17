
# adminpanel/views.py

from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from pages.models import Lead

from .models import (
    AdminProfile,
)


# =========================
# LOGIN
# =========================

def admin_login(request):

    if request.user.is_authenticated:

        return redirect('/admin/dashboard.html')

    if request.method == 'POST':

        username = request.POST.get('username')

        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('/admin/dashboard.html')

        else:

            return render(
                request,
                'adminpanel/admin-login.html',
                {
                    'error': 'Invalid Username or Password'
                }
            )

    return render(
        request,
        'adminpanel/admin-login.html'
    )


def mark_leads_as_read():
    Lead.objects.filter(
        is_read=True,
        status='New'
    ).update(status='Contacted')

    Lead.objects.filter(
        is_read=False,
        status='New'
    ).update(
        is_read=True,
        status='Contacted'
    )

    Lead.objects.filter(is_read=False).update(is_read=True)


# =========================
# DASHBOARD
# =========================

@login_required(login_url='/admin/admin-login.html')
def dashboard(request):

    context = {
        'total_leads': Lead.objects.count(),
        'recent_leads': Lead.objects.all().order_by('-id')[:5]
    }

    return render(
        request,
        'adminpanel/dashboard.html',
        context
    )


# =========================
# LEADS
# =========================



@login_required(login_url='/admin/admin-login.html')
def leads(request):
    mark_leads_as_read()

    leads = Lead.objects.all().order_by('-id')
    print("LEADS:", leads) # टर्मिनल में डेटा चेक करने के लिए सही है

    context = {
        'leads': leads
    }

    return render(
        request,
        'adminpanel/leads.html',
        context
    )



# =========================
# PROFILE
# =========================

@login_required(login_url='/admin/admin-login.html')
def profile(request):

    profile, created = AdminProfile.objects.get_or_create(
        user=request.user
    )

    if request.method == 'POST':

        username = request.POST.get('username')

        email = request.POST.get('email')

        password = request.POST.get('password')

        confirm_password = request.POST.get('confirm_password')

        profile_image = request.FILES.get('profile_image')

        request.user.username = username

        request.user.email = email

        if password and password == confirm_password:

            request.user.set_password(password)

        request.user.save()

        if profile_image:

            profile.profile_image = profile_image

            profile.save()

        return redirect('/admin/profile.html')

    context = {

        'profile': profile

    }

    return render(
        request,
        'adminpanel/profile.html',
        context
    )


# =========================
# LOGOUT
# =========================

def admin_logout(request):

    logout(request)

    return redirect('/admin/admin-login.html')

