from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound,NotAuthenticated,ParseError
from rest_framework.status import HTTP_204_NO_CONTENT
from .models import Room,Amenity
from categories.models import Category
from .serializers import amenitiySerializer,RoomSerializer,RoomDetailSerializer

class Amenities(APIView):

  def get(self,request):
    all_amenity = Amenity.objects.all()
    serializer = amenitiySerializer(all_amenity , many = True)
    return Response(serializer.data)

  def post(self,request):
    serializer = amenitiySerializer(data = request.data)
    if serializer.is_valid():
      created_data = serializer.save()
      return Response(amenitiySerializer(created_data).data)
    else: Response(serializer.errors)

class AmenityDetail(APIView):

  def get_object(self,pk):
    try: 
      return Amenity.objects.get(pk = pk)
    except Amenity.DoesNotExist:
      raise NotFound

  def get(self,request,pk):
    return Response(amenitiySerializer(self.get_object(pk)).data)
  
  def put(self,request,pk):
    amenity = self.get_object(pk)
    serializer = amenitiySerializer(amenity, data = request.data , partial = True)
    if serializer.is_valid():
      updated_data = serializer.save()
      return Response(amenitiySerializer(updated_data).data)
    else: return Response(serializer.errors)

  def delete(self,request,pk):
    amenity = self.get_object(pk)
    amenity.delete()
    return Response(status = HTTP_204_NO_CONTENT)

class Rooms(APIView):

  def get(self,request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many = True)
    return Response(serializer.data)
  
  def post(self,request):
    if request.user.is_authenticated:  #read_only여서 직접 validation진행한거임
      serializer = RoomDetailSerializer(data = request.data)

      if serializer.is_valid():
        category_pk = request.data.get("category")
        try: 
          category = Category.objects.filter(pk__in = category_pk)
          print(category.kind)  #instance여야 적용됨. 내일 amenity공부한 후 수정해보자
          if category.kind == Category.CategoryKindChoices.EXPERIENCE:
            raise ParseError
        except Category.DoesNotExist:
          raise NotFound
        

        created_data = serializer.save(owner = request.user , category = category)  # owner를 유저가 설정하면 안돼기 때문에 이렇게 한 거임.
        return Response(RoomDetailSerializer(created_data).data)
      else : return Response(serializer.errors)
    else: NotAuthenticated
class RoomDetail(APIView):

  def get_object(self,pk):
    try: 
      return Room.objects.get(pk=pk)
    except Room.DoesNotExist:
      raise NotFound
   
  def get(self,request,pk):
    room = self.get_object(pk)
    serializer = RoomDetailSerializer(room)
    return Response(serializer.data)
  

