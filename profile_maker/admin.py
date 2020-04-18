from django.contrib import admin
from .models import User_Profile
import os

admin.site.site_header = 'Admin Panel'


class User_ProfileAdmin(admin.ModelAdmin):
	list_display = ('Name','Email','Subject','Assignment','Time_of_Submission')

admin.site.register(User_Profile, User_ProfileAdmin)