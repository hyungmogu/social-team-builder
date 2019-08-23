from django.contrib import admin

from . import models

class ProfileAdmin(admin.ModelAdmin):
    fields = ['user','name','short_bio','profile_image','roles']
    list_display = ['user','name','short_bio','roles']
    list_editable = ['roles']

admin.site.register(models.Profile, ProfileAdmin)

