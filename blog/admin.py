from django.contrib import admin
from .models import Post, TimeTracker, Comment, Pinterest, RKGK, Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display=['id']

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'working', 'pub_date']

class TimeAdmin(admin.ModelAdmin):
    list_display = ['id', 'todaystart', 'switch']
    list_editable = ['todaystart', 'switch']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id']

class PinterestAdmin(admin.ModelAdmin):
    list_display = ['id', 'pin_url', 'pin_img']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(TimeTracker, TimeAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Pinterest, PinterestAdmin)
admin.site.register(RKGK)