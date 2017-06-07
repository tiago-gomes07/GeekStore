from django.contrib import admin
from .models import Banner

class BannerAdmin(admin.ModelAdmin):
	list_display = ['nome', 'image', 'promovido'] # campos que serão exibidos

admin.site.register(Banner, BannerAdmin)
