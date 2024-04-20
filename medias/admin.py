from django.contrib import admin
from .models import Photo,Video

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
  list_display = (
    "__str__",
    "room",
  )


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
  pass

