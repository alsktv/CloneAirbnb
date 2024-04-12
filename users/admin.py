from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
  fieldsets = (
    ("Profile",{"fields" : ("avater","username","password","name","email","is_host","gender","language","currency")},),
    ("permissions" , {"fields" : ("is_active","is_staff","is_superuser","groups","user_permissions",)}),
     ("Important datas",{"fields" : ("last_login",)})
  )
  list_display = [
    "username","name","email","last_login","is_host",
  ]
