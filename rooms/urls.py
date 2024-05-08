from django.urls import path
from .views import Amenities,AmenityDetail,Rooms,RoomDetail,Reviews,AmenitiesDetail,RoomPhotos,RoomBookings

urlpatterns = [
   path("amenities/",Amenities.as_view(), name = "amenities"), 
   path("amenities/<int:pk>/",AmenityDetail.as_view()),
   path("",Rooms.as_view()),
   path("<int:pk>",RoomDetail.as_view()),
   path("<int:pk>/reviews",Reviews.as_view()),
   path("<int:pk>/amenities",AmenitiesDetail.as_view()),
   path("<int:pk>/photos",RoomPhotos.as_view()),
   path("<int:pk>/bookings",RoomBookings.as_view()),
]