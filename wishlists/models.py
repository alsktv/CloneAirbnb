from django.db import models
from common.models import CommonModel

class Wishlist(CommonModel):
  """Wishlist"""

  name = models.CharField(max_length=150)
  rooms = models.ManyToManyField("rooms.Room",null=True , blank = True)
  experience = models.ManyToManyField("experiences.Experience",null=True , blank = True)
  user = models.ForeignKey("users.User", on_delete=models.CASCADE)

  def __str__(self):
    return self.name

