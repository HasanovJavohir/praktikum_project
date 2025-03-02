from django.contrib import admin
from .models import News, Category, Contact, Comment
# Register your models here.


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', "slug", "published_time", "status"]
    list_filter = ["status", "created_time", "published_time", "category"]
    prepopulated_fields = {"slug": ("title", )}
    date_hierarchy = "published_time"
    search_fields = ['title', "body", "category"]
    ordering = ['status', 'published_time']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['email']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'news', 'created_time', 'active']
    list_filter = ['created_time', 'active']
    search_fields = ['title', 'body']
    actions = ['disable_comments', 'activate_comments']


    def disable_comments(self, request, queryset):
        queryset.updte(active=False)

    def activate_comments(self, request, queryset):
        queryset.updte(active=True)
