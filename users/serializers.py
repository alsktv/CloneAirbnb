from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import User

class TinyUserSerializer(ModelSerializer):
  class Meta:
    model = User
    fields = (
      "name",
      "avater",
    )

class UserSerializer(ModelSerializer):


  class Meta:
    model = User
    exclude = [
      "password","is_superuser","name","user_permissions"
    ]

class ChangePasswordSerializer(ModelSerializer):
  class Meta:
    model:User
    fields = ["password"]