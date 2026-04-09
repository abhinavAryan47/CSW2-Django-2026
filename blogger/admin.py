from django.contrib import admin #type:ignore
from .models import Post, Comment
# Register your models here.
admin.site.register(Post)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=['name','email','post','created','active']
    list_filter=['created','active']
    search_fields=['name','email','body']