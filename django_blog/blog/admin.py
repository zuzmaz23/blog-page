from django.contrib import admin
from .models import Post, Comment, Like, Newsletter
from markdownx.admin import MarkdownxModelAdmin

@admin.register(Post)
class PostAdmin(MarkdownxModelAdmin):
    list_display = ('title', 'author', 'create_date', 'published_date')
    list_filter = ('create_date', 'published_date')
    search_fields = ('title', 'content')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_date', 'approved_comment')
    list_filter = ('approved_comment', 'created_date')
    search_fields = ('post', 'author')

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'created_date')

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_date', 'is_active')
    list_filter = ('is_active', 'subscribed_date')
    search_fields = ('email',)