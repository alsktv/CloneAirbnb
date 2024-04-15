from django.contrib import admin
from .models import Room, Amenity

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
  list_display = [
    "name","price","kind","owner","total_amenity","pet_allowed", "created_at",
    "updated_at","category",
  ]
  list_filter = [
    "country","city","price","rooms","pet_allowed","amenities","created_at"
  ]

  def total_amenity(self,room):  #self는 modelAdmin자체를 의미, room은 models를 의미함. 따라서 amenities같은 변수를 가져오기 위해서는 2번째 변수를 반드시 설정해 주어야 한다.
    return room.amenities.count()

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