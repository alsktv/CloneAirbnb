from django.utils import timezone
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Book
from users.serializers import TinyUserSerializer

class PublicBookingSerializer(ModelSerializer):
  
  user = TinyUserSerializer(read_only = True)
  class Meta:
    model = Book
    fields = (
      "user",
      "cheak_in",
      "cheak_out",
      "experience_time",
      "guests",
    )

class CreateRoomBookingSerializer(ModelSerializer):

    cheak_in = serializers.DateField() #이런 과정을 안해주면 밑에있는 Meta class가 먼저 적용되고, 이것은 model을 참조해서 serializer을 해줌. 하지만 이런식으로 overiding(덮어쓰기)를 해줌으로써 serializer되는 방식을 custom할 수 있음.
    cheak_out = serializers.DateField() #이런식으로 해주면 read_only하지 않는 이상은 반드시 이 값을 입력해야함

    def validate_cheak_in(self,value):  #value는 우리가 validation하고 싶은 값을 보내줌
       #이런식으로 validate_변수명 작성해주면 is_validated를 custom 할 수 있음
       now = timezone.localtime(timezone.now()).date()
       if now > value:
          raise serializers.ValidationError("is not validated") #validation이 안됐을때 나오는 문구
       return value #이렇게 return한 값이 속성값이 됨. return이 없으면 null 반환
       
    def validate_cheak_out(self,value):  #value는 우리가 validation하고 싶은 값을 보내줌
       now = timezone.localtime(timezone.now()).date()
       if now > value:
          raise serializers.ValidationError("is not validated") #validation이 안됐을때 나오는 문구
       return value

    def validate(self,data): #이 method는 모든 정보를 data에 담고 있고(dict형태), 이로 인해 모든 정보를 validation할 수 있음.
       if data["cheak_in"] and data["cheak_out"]:
        if data["cheak_in"] > data["cheak_out"]:
            raise serializers.ValidationError("cheak_in is should selected before cheak_out")
        if Book.objects.filter(cheak_in__lte = data["cheak_out"] , cheak_out__gte = data["cheak_in"] ).exists():
            raise serializers.ValidationError("The booking is already exist. please chose another date")

       else: serializers.ValidationError("test")

       return data # data를 그대로 return하면 validation이 된거임.

    class Meta:
      model = Book
      fields = (   
        "cheak_in",
        "cheak_out",
        "guests",
      )

class CreateExperienceBookingSerializer(ModelSerializer):

   user = TinyUserSerializer(read_only = True)
   experience_time = serializers.DateTimeField()

   def validate(self,data):
      now = timezone.localtime(timezone.now())
      if now > data.get("experience_time"):
         raise serializers.ValidationError("Past day can't select")
      return data
   class Meta:
      model = Book
      fields = (
         "user",
         "experience",
         "experience_time",
         "guests",
      )

class ExperienceBookDetailSerializer(ModelSerializer):
   user = TinyUserSerializer()
   class Meta:
      model = Book
      fields = "__all__"