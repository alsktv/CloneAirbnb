from django.db import models
from common.models import CommonModel

class Book(CommonModel):
  """Booking Model"""

  class BookKindChoices(models.TextChoices):
    ROOM = "room" , "Room" 
    EXPERIENCE = "experience" , "Experience"

  kind = models.CharField(max_length=10,choices=BookKindChoices.choices)

  user = models.ForeignKey("users.User",on_delete=models.CASCADE,related_name="books")

  room = models.ForeignKey("rooms.Room",on_delete=models.CASCADE, null=True , blank=True,related_name="books")

  experience =  models.ForeignKey("experiences.Experience",on_delete=models.CASCADE, null=True , blank=True,related_name="books")

  cheak_in = models.DateField(null=True,blank=True)
  cheak_out = models.DateField(null=True,blank=True)

  experience_time = models.DateTimeField(null=True,blank=True)

  guests = models.PositiveIntegerField()

  def __str__(self):
    return f"{self.user}/{self.kind.title()}/cheak in:{self.cheak_in}"

