from django.contrib import admin

# Register your models here.
from .models import userInfo

class userAdmin(admin.ModelAdmin):
	list_display = ('user_name','user_email', 'user_pass', 'user_mobile')

admin.site.register(userInfo, userAdmin)