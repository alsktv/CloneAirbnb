from django.db import models
from common.models import CommonModel

class Category(CommonModel):
  """ Room and Experience category"""

  class CategoryKindChoices(models.TextChoices):
    ROOM = "room" , "Room"
    EXPERIENCE = "experience" , "Experience"

  name = models.CharField(max_length=100)
  kind = models.CharField(max_length=10,choices= CategoryKindChoices.choices)

  def __str__(self):
    return f"{self.name} ({self.kind.title()})"
  
  class Meta:
    verbose_name_plural = "Categories"