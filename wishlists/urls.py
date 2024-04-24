from django.urls import path
from .views import WishLists,WishList
urlpatterns = [
  path("",WishLists.as_view()),
  path("<int:num>",WishList.as_view())
]