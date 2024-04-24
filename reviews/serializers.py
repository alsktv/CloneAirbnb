from rest_framework import serializers
from .models import Review
from users.serializers import TinyUserSerializer

class reviewSerializer(serializers.ModelSerializer):

  user = TinyUserSerializer(read_only = True)

  class Meta:
    model = Review
    fields = ["user",
              "experience",
              "user_rating",
              "room",
              ]
