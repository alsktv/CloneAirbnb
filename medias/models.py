from django.db import models
from common.models import CommonModel

class Photo(CommonModel):
  file = models.URLField()
  description = models.CharField(max_length=200)
  room = models.ForeignKey("rooms.Room",on_delete=models.CASCADE,null=True,blank=True, related_name = "photo" )
  experience = models.ForeignKey("experiences.Experience", on_delete = models.CASCADE,
  null = True , blank = True)

  def __str__(self):
    return self.description


class Video(CommonModel):
  file = models.URLField()
  experience = models.OneToOneField("experiences.Experience",on_delete=models.CASCADE)

  def __str__(self):
    return "Video"