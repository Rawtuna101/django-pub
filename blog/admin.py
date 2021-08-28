from django.contrib import admin
from .models import Post, TimeTracker, Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'working', 'pub_date']

class TimeAdmin(admin.ModelAdmin):
    list_display = ['id', 'todaystart', 'switch']
    list_editable = ['todaystart', 'switch']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'comment_user']

admin.site.register(Post, PostAdmin)
admin.site.register(TimeTracker, TimeAdmin)
admin.site.register(Comment, CommentAdmin)