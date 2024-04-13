from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
  list_display = (
    "__str__",
    "room",
    "experience",
    "guests",
  )
  list_filter = (
    "kind",
  )
