from django.contrib import admin
from .models import User

# Register your users here.
@admin.register(User)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'password']
    pass