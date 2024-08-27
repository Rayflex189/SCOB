from django.contrib import admin

# Register your models here.

from .models import *

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'account_number', 'otp_code', 'imf_code', 'aml_code', 'tac_code', 'vat_code']  # Specify fields to display in the admin list
    search_fields = ['user__username']  #

class YourModelAdmin(admin.ModelAdmin):
    list_display = ('image_display')

    def image_display(self, obj):
        return obj.image.url if obj.image else None


