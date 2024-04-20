from django.urls import path
from .views import Amenities,AmenityDetail,Rooms,RoomDetail,Reviews,AmenitiesDetail,RoomPhotos

urlpatterns = [
   path("amenities/",Amenities.as_view()), 
   path("amenities/<int:pk>/",AmenityDetail.as_view()),
   path("",Rooms.as_view()),
   path("<int:pk>",RoomDetail.as_view()),
   path("<int:pk>/reviews",Reviews.as_view()),
   path("<int:pk>/amenities",AmenitiesDetail.as_view()),
   path("<int:pk>/photos",RoomPhotos.as_view()),
]