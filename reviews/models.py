from django.db import models
from common.models import CommonModel

class Review(CommonModel):
  """ user review that leave to rooms or experiences"""

  user = models.ForeignKey("users.User",on_delete=models.CASCADE)

  room = models.ForeignKey("rooms.Room",null=True,blank=True,on_delete=models.CASCADE)

  experience = models.ForeignKey("experiences.Experience",null=True,blank=True,on_delete=models.CASCADE)

  user_review = models.TextField()

  user_rating = models.PositiveIntegerField()

  def __str__(self):
    return f"{self.user} : {self.user_rating}"
 