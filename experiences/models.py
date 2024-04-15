from django.db import models
from common.models import CommonModel

class Experience(CommonModel):
  country = models.CharField(max_length=50, default="korea")
  city = models.CharField(max_length=40,default="seoul")
  name = models.CharField(max_length=200,default="")
  host = models.ForeignKey("users.User",on_delete=models.CASCADE,related_name="experiences")
  price = models.PositiveIntegerField()
  adress = models.CharField(max_length=150)
  start_at = models.TimeField()
  end_at = models.TimeField()
  description = models.TextField()
  perk = models.ManyToManyField("experiences.Perk",related_name="experiences")
  category = models.ForeignKey("categories.Category",on_delete=models.SET_NULL,null=True , blank=True,related_name="experiences")
  

  def __str__(self):
    return self.name

class Perk(CommonModel):
  """ It is introduce that what the experience include"""

  name = models.CharField(max_length=100)
  detail = models.CharField(max_length=150)
  explanation = models.TextField()
  
  def __str__(self):
    return self.name


