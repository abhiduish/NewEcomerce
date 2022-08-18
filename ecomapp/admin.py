from django.contrib import admin
from .models import Customuser


class CustomAdmin(admin.ModelAdmin):
    list_display = ('usertype','gender')


admin.site.register(Customuser, CustomAdmin)