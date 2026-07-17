from pages.models import Lead

from .models import AdminProfile


def admin_panel_context(request):
    if not request.path.startswith('/dashboard/') and not request.path.startswith('/admin/'):
        return {}

    context = {
        'total_leads': Lead.objects.count(),
        'new_leads': Lead.objects.filter(is_read=False).count(),
        'latest_unread_leads': Lead.objects.filter(is_read=False).order_by('-created_at')[:5],
    }

    if request.user.is_authenticated:
        profile, _ = AdminProfile.objects.get_or_create(user=request.user)
        context['profile'] = profile

    return context
