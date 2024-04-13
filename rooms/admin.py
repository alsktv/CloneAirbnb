from django.contrib import admin
from .models import Room, Amenity

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
  list_display = [
    "name","price","kind","owner","pet_allowed", "created_at",
    "updated_at","category",
  ]
  list_filter = [
    "country","city","price","rooms","pet_allowed","amenities","created_at"
  ]

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
  list_display = [
    "name",
    "description",
    "created_at",
    "updated_at",
  ]
  readonly_fields = [
    "created_at",
    "updated_at",
  ]