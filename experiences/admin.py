from django.contrib import admin
from .models import Experience,Perk

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
  list_display = (
  "country",
  "city",
  "name",
  "host",
  "price",
  )

@admin.register(Perk)
class PerkAdmin(admin.ModelAdmin):
  pass




