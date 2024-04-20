from rest_framework.serializers import ModelSerializer
from .models import Photo
from rooms.serializers import RoomSerializer

class PhotoSerializer(ModelSerializer):  #serializer는 유효성을 검사하는 역할도 한다.
  room = RoomSerializer(read_only = True)

  class Meta:
    model = Photo
    fields = (
      "pk",
      "file",
      "description",
      "room",
    )