from django.conf import settings
from django.db import transaction
from django.utils import timezone   #시간과 관련된 라이브러리
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound,NotAuthenticated,ParseError,PermissionDenied
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Room,Amenity
from .serializers import amenitiySerializer,RoomSerializer,RoomDetailSerializer
from categories.models import Category
from books.models import Book
from books.serializers import PublicBookingSerializer,CreateRoomBookingSerializer
from reviews.serializers import reviewSerializer
from medias.serializers import PhotoSerializer

class Amenities(APIView):

  permission_classes = [IsAuthenticatedOrReadOnly] #이걸 해주면 authenticated를 검사할 필요 없음

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

  permission_classes = [IsAuthenticatedOrReadOnly]


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

  permission_classes = [IsAuthenticatedOrReadOnly]

  def get(self,request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many = True)
    return Response(serializer.data)
  
  def post(self,request):
    if request.user.is_authenticated:  #read_only여서 직접 validation진행한거임
      serializer = RoomDetailSerializer(data = request.data)

      if serializer.is_valid():

                 ##### category를 만드는 코드 ####
        category_pk= request.data.get("category")

        if not category_pk:
            raise ParseError
        try:
          category = Category.objects.get(pk= category_pk)  
          if category.kind == Category.CategoryKindChoices.EXPERIENCE:
              raise ParseError("category kindis should be room")  
        except Category.DoesNotExist:
          raise ParseError  
        try:      
          with transaction.atomic():
              created_data = serializer.save(owner = request.user , category = category ) # owner를 유저가 설정하면 안돼기 때문에 이렇게 한 거임.  

          ####amenities를 만드는 코드 ####
              amenities = request.data.get("amenities")  #pk가 들어가 있는 리스트임
              for amenities_pk in amenities:
                  amenity = Amenity.objects.get(pk = amenities_pk)
                  created_data.amenities.add(amenity)

              return Response(RoomDetailSerializer(created_data).data)
        except Exception:
          raise ParseError()

  
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

  def put(self,request,pk):
    room = self.get_object(pk)
    if request.user.is_authenticated:
      raise NotAuthenticated
    if room.owner != request.user:  #request.user도 serializer를 반여한 dict형태로 반환 됨
      raise PermissionDenied
    serializer = RoomDetailSerializer(room , data = request.data , partial = True)

    
    if serializer.is_valid():
      category_pk = request.data.get("category")
      try:
        category = Category.objects.get(pk = category_pk)
        
      except Category.DoesNotExist:
        raise NotFound
      updated_data = serializer.save(category = category)
      
      amenities_pk = request.data.get("amenities")
      if len(amenities_pk) != 0:
        updated_data.amenities.clear()
        for pk in amenities_pk:
          try:

            amenity = Amenity.objects.get(pk = pk)
            print(amenity)
            updated_data.amenities.add(amenity)
          except Amenity.DoesNotExist:
            raise NotFound
        

      
      return Response(RoomDetailSerializer(updated_data).data)

  
  def delete(self,request,pk):
    room = self.get_object(pk)
    if request.user.is_authenticated:
      raise NotAuthenticated
    if room.owner != request.user:  #request.user도 serializer를 반여한 dict형태로 반환 됨
      raise PermissionDenied
    room.delete()
    return Response(status = HTTP_204_NO_CONTENT )
  
class Reviews(APIView):
  permission_classes = [IsAuthenticatedOrReadOnly]

  def get_object(self,pk):
    try:
      room = Room.objects.get(pk = pk)
      return room.reviews.all()  #역 연산자로 값을 가져오면 그 값은 queryset이 됨. 이 쿼리셋 값을 가져오기 위해서는 뒤에 all()을 붇여줘야함. ORM에 사용하는 all() 과는 다름.
    except Room.DoesNotExist:
      raise NotFound
    
  def get(self,request,pk):
    try:
      # print(request.query_params) #url에 있는 params값을 가져와줌 . ? 뒤에 있는 값을 의미함
      page = request.query_params.get("page",1) #get()은 dict에서 활용 가능, 또한 default도 지정 가능.따라서 입력을 안했을때는 1페이지로 가게 만듬
      page = int(page) #get()으로 가져온 값은 string이기 때문에  int로 바꿔줌
      page_size = 3
      reviews = self.get_object(pk)
      serializer = reviewSerializer(reviews[page*page_size-3:page*page_size], many = True)
      return Response(serializer.data)
    except ValueError: #except에는 에러가 나왔을 때 그 애러의 이름을 그대로 적어주면 됨***
      page = 1

  def post(self,request,pk):
    serializer = reviewSerializer(data = request.data)
    user = request.user
    if serializer.is_valid():
      created_data = serializer.save(user = user, room = self.get_object(pk))
      return Response(reviewSerializer(created_data).data)
    else:
      return serializer.errors


class AmenitiesDetail(APIView):
  def get_object(self,pk):
    room = Room.objects.get(pk = pk)
    amenities = room.amenities
    serializer = amenitiySerializer(amenities, many = True) # many = True 안하면 null로 보임
    return serializer.data
  
  def get(self,request,pk):
    amenities = self.get_object(pk)
    content_count = settings.PAGE_WIDTH #settings는 objects임
    try: 
      page = int(request.query_params.get("page",1))

    except ValueError:
      page = 1

    return Response(amenities[page*content_count - 3 : page*content_count])
  
class RoomPhotos(APIView):
  def get_objects(self,pk):  #get_object는 굳이 serializer할 필요 없음
    try:
      room = Room.objects.get(pk = pk)
      return room
    except Room.DoesNotExist:
      raise NotFound
    

  def post(self,request,pk):
    room = self.get_objects(pk)
    if not request.user.is_authenticated:
      return NotAuthenticated
    if request.user != room.owner:
      raise PermissionDenied
    serializer = PhotoSerializer(data = request.data)
    if serializer.is_valid():
      created_data = serializer.save(room = room )
      return Response(PhotoSerializer(created_data).data)
    else: return Response(serializer.errors)
      
class RoomBookings(APIView):
  permission_classes = [IsAuthenticatedOrReadOnly]

  def get_objects(self,pk):
    try:
      return Room.objects.get(pk = pk) #objects는모델데이터를 ORM으로 바꿔주는 역할을 한다.
    except:
      raise NotFound
    

  def get(self,request,pk):
   now_date = timezone.localtime(timezone.now()).date() #timezone.now() 를 하면 현재 날짜와 시간을 둘다 보여줌. localtime은 현재 지역의 날짜와 시간을 알려주고, date()는 날짜만 가져오게 만들어줌
   bookings = Book.objects.filter(room__pk = pk , kind = Book.BookKindChoices.ROOM , cheak_in__gt = now_date) #if,else쓰는 것보다 훨씬 간편함
   serializer = PublicBookingSerializer(bookings, many = True) #serializer는 queryset과 JSON과의 관계이다.
   return Response(serializer.data)
  
  def post(self,request,pk):
    room = self.get_objects(pk)
    serializer = CreateRoomBookingSerializer(data = request.data)
    print(serializer)
    if serializer.is_valid():
      created_data = serializer.save(
        room = room,
        user = request.user,
        kind = Book.BookKindChoices.ROOM,
      )
      return Response(PublicBookingSerializer(created_data).data)

    else: 
      return Response(serializer.errors)