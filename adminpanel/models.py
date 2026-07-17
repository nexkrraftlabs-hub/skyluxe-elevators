# adminpanel/models.py

from django.db import models
from django.contrib.auth.models import User



class AdminProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    profile_image = models.ImageField(
        upload_to='profile/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.user.username

    def _default_avatar_url(self, size=None):
        username = self.user.get_username() or 'Admin'
        url = (
            'https://ui-avatars.com/api/?name='
            f'{username}&background=152270&color=ffffff'
        )
        if size:
            url = f'{url}&size={size}'
        return url

    @property
    def avatar_url(self):
        if self.profile_image and self.profile_image.name:
            try:
                if self.profile_image.storage.exists(self.profile_image.name):
                    return self.profile_image.url
            except (ValueError, OSError):
                pass
        return self._default_avatar_url()

    @property
    def avatar_url_large(self):
        if self.profile_image and self.profile_image.name:
            try:
                if self.profile_image.storage.exists(self.profile_image.name):
                    return self.profile_image.url
            except (ValueError, OSError):
                pass
        return self._default_avatar_url(size=200)