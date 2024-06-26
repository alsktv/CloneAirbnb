from django.contrib import admin
from .models import House

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
  list_display = ("name","price_per_night","pet_allowed","owner",)