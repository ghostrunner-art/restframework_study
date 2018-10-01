from django.contrib import admin
from .models import UserInfo,UserGroup,Role

class UserInfoadmin(admin.ModelAdmin):
    list_display = ('user_name','user_group')

admin.site.register(UserInfo,UserInfoadmin)
admin.site.register(UserGroup)
admin.site.register(Role)