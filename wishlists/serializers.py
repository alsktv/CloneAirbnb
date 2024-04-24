from rest_framework.serializers import ModelSerializer
from .models import Wishlist
from users.serializers import TinyUserSerializer
from rooms.serializers import RoomSerializer
from experiences.serializers import ExperienceSerializer

class WishListSerializer(ModelSerializer):

  user = TinyUserSerializer(read_only = True)
  room = RoomSerializer(many = True, read_only = True)  #save에 정보를 넣기 위해서는 반드시 read_only = True 를 해주어야 함.
  experience = ExperienceSerializer(many = True , read_only = True)


  class Meta:
    model = Wishlist
    fields = [
      "name",
      "user",
      "room",
      "experience",
    ]
