from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ParseError
from .models import Perk,Experience
from datetime import datetime


class PerkSerializer(ModelSerializer):
  class Meta:
    model = Perk
    fields = "__all__"

class ExperienceSerializer(ModelSerializer):

  def validate(self,data):
    now = datetime.now().date()
    if data["date"] <  now:
      raise ParseError("past date can't select")
    return data
  
  perk = PerkSerializer(many = True)

  class Meta:
    model = Experience
    fields = "__all__"

class TinyExperienceSerializer(ModelSerializer):
  class Meta:
    model = Experience
    fields = (
      "country",
      "city",
      "name",
      "host",
    )