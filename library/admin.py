from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_recommended', 'created_at')
    list_filter = ('is_recommended',)
    search_fields = ('title', 'author', 'description')
