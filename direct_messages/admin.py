from django.contrib import admin
from .models import Cheating_Room,Message

@admin.register(Cheating_Room)
class CheatingRoomAdmin(admin.ModelAdmin):
  list_display = (
    "__str__",
    "created_at",
  )


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
  list_display = (
    "text",
    "user",
    "room",
    "created_at",

  )
  list_filter = (
    "created_at",
    "room",
  )