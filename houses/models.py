from django.db import models
from common.models import CommonModel

class House(CommonModel):
  name = models.CharField(max_length=140)
  price_per_night = models.PositiveIntegerField()
  description = models.TextField()
  adress = models.CharField(max_length=140)
  pet_allowed = models.BooleanField(default=True)
  owner = models.ForeignKey("users.User",on_delete=models.CASCADE, null=True)

  def __str__(self):
    return self.name
1