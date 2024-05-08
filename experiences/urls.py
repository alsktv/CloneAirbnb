from django.urls import path
from .views import Perks, PerkDetail,Experiences,ExperienceDetail,ExperiencePerk,Bookings,BookDetail

urlpatterns = [
  path("",Experiences.as_view()),
  path("<int:pk>",ExperienceDetail.as_view()),
  path("perks/",Perks.as_view()),
  path("perks/<int:pk>/",PerkDetail.as_view()),
  path("<int:pk>/perks", ExperiencePerk.as_view() ), #이거는 한개의 experience의 perk전부를 보여주는 것임.
  path("<int:pk>/bookings", Bookings.as_view()),
  path("<int:pk>/bookings/<int:bookPk>",BookDetail.as_view())
]