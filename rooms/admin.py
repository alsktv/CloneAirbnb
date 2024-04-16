from django.contrib import admin
from .models import Room, Amenity

@admin.action(description="set all price to zero")
def reset_price(modal_admin,request,rooms):
  for room in rooms:
    room.price = 0
    room.save()

@admin.action(description="plus price 5")
def add_5(modal_admin,request,rooms):
  for room in rooms:
    room.price += 5
    room.save()

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

  actions = (reset_price,add_5,)

  list_display = [
    "name","price","kind","owner","total_amenity","pet_allowed", "created_at",
    "avg_rating"
  ]
  list_filter = [
    "country","city","price","rooms","pet_allowed","amenities","created_at"
  ]

  search_fields = (
    "name",
    "price",
    "=owner__username",
  )

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