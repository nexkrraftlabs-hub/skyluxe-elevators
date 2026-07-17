"""
URL configuration for skyluxe_site project.
"""

from django.contrib import admin

from django.urls import path, include

from django.conf import settings

from django.conf.urls.static import static


urlpatterns = [
        # FRONTEND WEBSITE

    path('', include('pages.urls')),

    # DJANGO ADMIN

    path('django-admin/', admin.site.urls),

    # CUSTOM ADMIN PANEL

    path('admin/', include('adminpanel.urls')),

]

# MEDIA FILES

urlpatterns += static(

    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT

)
