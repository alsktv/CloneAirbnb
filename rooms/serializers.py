from rest_framework.serializers import  ModelSerializer
from  .models import Room,Amenity
from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer
class amenitiySerializer(ModelSerializer):
  class Meta:
    model = Amenity
    fields = ("name",
              "description",
              )
    depth = 1

class RoomSerializer(ModelSerializer):
  class Meta:
    model = Room
    fields = ["name",
              "country",
              "city",
              "price",
              ]

class RoomDetailSerializer(ModelSerializer):
  owner = TinyUserSerializer(read_only = True)
  amenities = amenitiySerializer(read_only = True , many = True)
  category = CategorySerializer(read_only = True , many = True)

  class Meta:
    model = Room
    fields = "__all__"

  def create(self,validated_data):
    return Room.objects.create(**validated_data)  #create()의 결과는 instance임 따라서 return되는 값 역시 instance임

