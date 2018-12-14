# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from mainpage.models import UserInfo
from mainpage.models import Task
# Register your models here.
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('user','age','phone')
    ordering = ['age',]
    search_fields = ('age','phone')
admin.site.register(UserInfo,UserInfoAdmin)

class TaskAdmin(admin.ModelAdmin):
    list_display = ('pusher','receiver','task','date')
    ordering = ['date',]
admin.site.register(Task,TaskAdmin)