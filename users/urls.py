from django.urls import path
from . import views

urlpatterns = [ 
  path("me",views.Me.as_view()), #urlpatterns에 있는 리스트 순서대로 url검사함. 따라서 <str:username> 을 "me" 앞에 두면 username이 me인 것을 찾을 것임.
  path("",views.Users.as_view()),
  path("@<str:username>",views.Username.as_view()) , #이런식을<>주변에 글짜 넣는것도 가능!!!
  path("change-password",views.ChangePassword.as_view()),
  path("log-in",views.LogIn.as_view()),
  path("log-out", views.LogOut.as_view()),
]