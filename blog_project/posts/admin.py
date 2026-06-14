
from django.contrib import admin
from .models import BlogPostModel

@admin.register(BlogPostModel)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'published_at')
    search_fields = ('title', 'content')
    list_filter = ('published_at', 'created_at')