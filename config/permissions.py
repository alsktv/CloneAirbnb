import jwt
from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed 
from users.models import User
class TrustMeBroAuthentication(BaseAuthentication):  #custom된 인증을 만드는 방법

  def authenticate(self,request):
    username = request.headers.get("Trust_Me","alsktv")
    print(request.headers)
    if not username:
      return None  #none을 받으면 다음 인증을 실행함.
    try:
      user = User.objects.get(username = username)
      return (user,None) #튜플을 보내주어야함.
    except User.DoesNotExist:
      raise AuthenticationFailed(f"No User{username}")
    
class JWTAuthentication(BaseAuthentication):

  def authenticate(self,request):
    token = request.headers.get("Authorization")
    if not token:
      return None
    decode =  jwt.decode(token,settings.SECRET_KEY , algorithms = ["HS256"] ) #decode 를 해주면 우리가 처음에 토큰을 만들 때 집어넣었던 dict가 그대로 출력됨!!!
    # print(decode)
    pk = decode.get("pk")
    if not pk:
      raise AuthenticationFailed("Invalid Token") #authenticate할때 사용할 수 있는 exception임
    else:
      try:
        user = User.objects.get(pk = pk)
        return (user,None)
      except User.DoesNotExist:
        raise AuthenticationFailed("User Not Found")
