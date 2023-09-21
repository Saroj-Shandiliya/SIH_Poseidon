# # console/admin.py

# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin  # Import UserAdmin
# from .models import CustomUser

# class CustomUserAdmin(UserAdmin):  # Inherit from UserAdmin
#     model = CustomUser

# admin.site.register(CustomUser, CustomUserAdmin)

# console/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserAdminForm

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'zoneID', 'secretKey', 'is_staff')


admin.site.register(CustomUser, CustomUserAdmin)
