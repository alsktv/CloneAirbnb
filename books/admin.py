from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
  def delete_all_books(self,request,queryset):  #admin함수는 3가지를 기본 인자로 가짐. queryset은 유저가 선택한 인스턴스를 모아놓은 queryset을 반환해준다.
    Book.objects.all().delete()
    
  list_display = (
    "__str__",
    "room",
    "experience",
    "guests",
  )
  list_filter = (
    "kind",
  )
  actions = [ "delete_all_books",]  #리스트가 아니라 tuple로 하면 에러남 . 그리고 action이 아닌 actions임을 기역하자.