# admin.py
from django.contrib import admin
from .models import UserDetail
from django.utils.html import format_html

class UserDetailAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'sex', 'mobile', 'address', 'photo_thumbnail')
    list_filter = ('sex', 'age')
    search_fields = ('name', 'mobile', 'address')

    def photo_thumbnail(self, obj):
        if obj.photo:
            return format_html('<img src="{}" style="width: 50px; height: 50px;" />'.format(obj.photo.url))
        return "No Image"
    photo_thumbnail.short_description = 'Photo'

admin.site.register(UserDetail, UserDetailAdmin)
