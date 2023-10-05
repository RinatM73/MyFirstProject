from django.contrib import admin

from .models import News, Comment

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title","date")

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'created_date')
admin.site.register(Comment, CommentAdmin)
