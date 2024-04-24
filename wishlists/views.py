from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound # status 는 HTTP임
from rest_framework.status import HTTP_204_NO_CONTENT
from users.models import User
from rooms.models import Room
from .models import Wishlist
from .serializers import WishListSerializer

class WishLists(APIView):
  """ 유저가 맍든 wishlist 전부를 보여주는 class"""
  def get(self,request):
    user = User.objects.get(pk = request.user.pk)
    wishlist = user.wishlists.all()
    return Response(WishListSerializer(wishlist , many = True).data)

  def post(self,request):
    serializer = WishListSerializer(data = request.data)
    room_pk = request.data["room"]
    rooms = [Room.objects.get(pk = room) for room in room_pk]

    if serializer.is_valid():
      created_data = serializer.save(user = request.user , room = rooms)
      return Response(WishListSerializer(created_data).data)
    else:
      return Response(serializer.errors)

class WishList(APIView):
  """ 유저가 만든 wishlist중 한개를 보여주는 class"""
  def get_objects(self,request,num):
    try:
      user = User.objects.get(pk = request.user.pk)
      wishlist = user.wishlists.all()
      return wishlist[num-1]  #이렇게 리스트로 만드는 것보다 filter이용하는 게 더 나음. filter라는 것은 특정 속성의 값을 이용하여 찾는 거임. lookup역시 이용가능.
    except Wishlist.DoesNotExist :
      raise NotFound
  
  def get(self,request,num):
    Wishlist = self.get_objects(request,num)
    serializer = WishListSerializer(Wishlist)
    return Response(serializer.data)
  
  def put(self,request,num):
    Wishlist = self.get_objects(request,num)
    serializer = WishListSerializer(Wishlist,data = request.data , partial = True)
    #room모델을 pk값만 입력할 수 있게 만듬
    room_pk = request.data["room"]
    rooms = [Room.objects.get(pk = room) for room in room_pk]
      #experience 모델을 pk값만 입력할 수 있게 만듬
    experience_pk = request.data["experience"]
    experiences = [Room.objects.get(pk = expoerience) for expoerience in experience_pk]
    if serializer.is_valid():
      updated_data = serializer.save(user = request.user , room = rooms , experience = 
                                     experiences)
      return Response(WishListSerializer(updated_data).data)
    else:
      return Response(serializer.errors)
    
  def delete(self,request,num):
    wishlist = self.get_objects(request,num)
    wishlist.delete()
    return Response(status = HTTP_204_NO_CONTENT)


