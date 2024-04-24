from rest_framework.serializers import  ModelSerializer
from rest_framework import serializers
from .models import Room,Amenity
from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer
from reviews.serializers import reviewSerializer



class amenitiySerializer(ModelSerializer):
  class Meta:
    model = Amenity
    fields = ("name",
              "description",
              )
    depth = 1

class RoomSerializer(ModelSerializer):
  rating = serializers.SerializerMethodField()
  # photos = PhotoSerializer(many = True, read_only = True)

  def get_rating(self,room) :
    return room.avg_rating() 
  class Meta:
    model = Room
    fields = ["name",
              "country",
              "city",
              "price",
              "rating",
              ]

class RoomDetailSerializer(ModelSerializer):
  owner = TinyUserSerializer(read_only = True)
  # amenities = amenitiySerializer(read_only = True , many = True)
  category = CategorySerializer(read_only = True ) #foreignkey에 many=True 적으면 iterable에러 남
  photos = serializers.SerializerMethodField()
  def get_photos(self,room):  #query-set은 serializing(직렬화)가 안됨.리스트로 바꿔줘야 함
    photos =  room.photos()
    list_photos = [{"file":photo.file , "description":photo.description }for photo in photos]
    return list_photos
  
  rating = serializers.SerializerMethodField()  #커스텀할 변수를 설정하고 method를 받는다고 선언함. 이후 get_rating이라는 method를 정의하면 그 함수의 return값이 이변수에 들어가게 됨. 반드시 함수 이름은 get_rating이여야함. get_ 이 아니면 안됨**!!

  def get_rating(self,room) : #여기서 room 은 우리가 custom variable을 만들때와 동일하게 instance를 받는다. 따라서 object에서 사용하는 거 사용 가능. 이걸 이용해 커스텀된 변수값을 화면에 나타낼 수 있음
    return room.avg_rating()  #method 호출할 때는 반드시() 붙이기
  
 # reviews = reviewSerializer(many = True , read_only = True) #many = True는 serializer에서 사용하는 property임. serializer에 들어가는 값이 1개보다 많을 때는 반드시 사용해 주어야함.
  # 추가로 django는 reverse를 자동으로 저장하기에 related_name인 reviews가 자동으로 저장되어 있음. 따라서 위와 같은 문장으로 사용해도 됨



  class Meta:
    model = Room
    fields = "__all__"

  def create(self,validated_data):
    return Room.objects.create(**validated_data)  #create()의 결과는 instance임 따라서 return되는 값 역시 instance임


