from django.db import models
from common.models import CommonModel

class Wishlist(CommonModel):
  """Wishlist"""

  name = models.CharField(max_length=150)
  room = models.ManyToManyField("rooms.Room",null=True , blank = True, related_name="wishlists")
  experience = models.ManyToManyField("experiences.Experience",null=True , blank = True, related_name="wishlists")
  user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="wishlists")

  def __str__(self):
    return self.name

