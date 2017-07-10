from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import MyUser
from django.utils.translation import ugettext_lazy as _


class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password', 'img_profile')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(MyUser, MyUserAdmin)