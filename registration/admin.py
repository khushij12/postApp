from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(userInfo)
admin.site.register(User)

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     pass

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     pass

# @admin.register(comment)
# class CommentAdmin(admin.ModelAdmin):
#     pass