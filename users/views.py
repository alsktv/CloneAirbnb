from django.contrib.auth import authenticate,login,logout
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ParseError,NotFound
from .serializers import UserSerializer,ChangePasswordSerializer
from users.models import User

class Me(APIView):
  permission_classes = [IsAuthenticated]

  def get(self,request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)
  
  def put(self,request):
    user = request.user
    serializer = UserSerializer(user , data = request.user , partial = True)
    if serializer.is_valid():
      updated_data = serializer.save()
      return Response(UserSerializer(updated_data).data)
    
class Users(APIView):
  def post(self,request):
    password = request.data.get("password")
    if not password:
      raise ParseError("password should be written")
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
      created_data = serializer.save()
      created_data.set_password(password)  #비밀번호를 해시화 시키는 과정
      created_data.save()
      return Response(UserSerializer(created_data).data) #serializer를 잘못하면 "" is not attribute에러가 뜸. 모델에 정의 잘 했는대, 이런 에러가 뜨면 serializer에 재대로 정보를 넣어줬는지 확인해보자.
    else:
      return Response(serializer.errors)

class Username(APIView):

  def get(self,request,username):
    try:
      user = User.objects.get(username = username)
      return Response(UserSerializer(user).data)
    except User.DoesNotExist:
      raise NotFound
    
class ChangePassword(APIView):

  permission_classes = [IsAuthenticated]
  
  def put(self,request):
    user = request.user
    old_password = request.user.get("old_password")
    new_password = request.user.get("nwe_password")
    if not old_password or not new_password:
      raise ParseError("please wirte old and new password")
    if user.cheak_password(old_password):
      user.set_password(new_password)
      user.save()
      return Response(status = status.HTTP_200_OK)
    else:
      return Response(status = status.HTTP_400_BAD_REQUEST)
    
class LogIn(APIView):

    def post(self,request):
       username = request.data.get("username")
       password = request.data.get("password")
       if not username or not password:
         raise ParseError
       user = authenticate(request,username = username , password = password)
       if user:
         login(request,user)
       else:
         return Response({"error":"wrong password"})
       
class LogOut(APIView):

  Permission_classes = [IsAuthenticated]

  def post(self,request):
    logout(request)
    return Response({"status" : "logout is succesful"})
