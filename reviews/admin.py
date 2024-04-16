from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from .models import Review

class WorldFilter(admin.SimpleListFilter):
  title = "Filter by word"
  parameter_name = "word"

  def lookups(self,request,modal_admin):
    return [
      (
       "good","Good",
    ),
    ("great","Great"),
    ("awsome","awsome"),
    ]
  
  def queryset(self,request,reviews):
    word = self.value()
    if word is not None:  #self.value로 가져온 값도 존재유무를 if 문을 이용해 확인해야함
        if reviews.exists():
            return reviews.filter(user_review__contains=word)
    return reviews.none()
  
class Classfy_rating(admin.SimpleListFilter):
     title = "good or bad review"
     parameter_name = "review"

     def lookups(self, request, modal_admin):
        return [
           ("good","Good(over4)"),
           ("bad","Bad(under4)"),
        ]
     
     def queryset(self, request, reviews):
        word = self.value()
        if word is not None:  
          if reviews.exists():
            if word == "good" :
              return reviews.filter(user_rating__gte = 4)
            else:
               return reviews.filter(user_rating__lt = 4)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
  list_display = (
    "__str__",
    "room",
    "experience",
    "created_at",
  )
  list_filter = (
    "user_rating",
    "user__is_host",
    "room__category",
    WorldFilter,
    Classfy_rating,
  )
