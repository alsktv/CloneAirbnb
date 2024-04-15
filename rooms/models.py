from django.db import models
from common.models import CommonModel

class Room(CommonModel):

  class RoomKindChoices(models.TextChoices):
    ENTIRE_PLACE = ("entire_place","Entire Place")
    PRIVATE_ROOM = ("private_room","Private Room" )
    SHARED_ROOM = ("shared_room","Shared Room")
  country = models.CharField(max_length=50, default="korea")
  city = models.CharField(max_length=40,default="seoul")
  name = models.CharField(max_length=100,default="")
  price = models.PositiveIntegerField()
  rooms = models.PositiveIntegerField()
  toilets = models.PositiveIntegerField()
  adress = models.CharField(max_length=200)
  pet_allowed = models.BooleanField(default=False)
  kind = models.CharField(max_length=20,choices=RoomKindChoices.choices)
  owner = models.ForeignKey("users.User",on_delete=models.CASCADE , related_name = "rooms")
  amenities = models.ManyToManyField("rooms.Amenity",related_name="rooms")
  category = models.ForeignKey("categories.Category",on_delete=models.SET_NULL,null=True , blank=True,related_name="rooms")
  
  def __str__(self):
    return self.name
  

  


  

  

class Amenity(CommonModel):
  """Amenity definition"""

  name = models.CharField(max_length=150)
  description = models.TextField(default="",null=True,blank=True)

  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name_plural = "Amenities"
