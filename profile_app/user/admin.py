from django.contrib import admin
from user.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


class UserProfileInline(admin.StackedInline):
    """Inline class to add the UserProfile model to the User admin page."""
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'userprofile'


class UserAdmin(UserAdmin):
    """Class to add the UserProfile model to the User admin page."""
    inlines = (UserProfileInline, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)