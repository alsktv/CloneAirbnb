from django.urls import path
from .views import PhotoDetail

urlpatterns = [
  path("<int:pk>",PhotoDetail.as_view()),
]