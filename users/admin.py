from django.contrib import admin
from users.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'telegram', 'website', 'created_at')
    search_fields = ('user__username', 'telegram')
