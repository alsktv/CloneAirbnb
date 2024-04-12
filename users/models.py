from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

  class GenderChoices(models.TextChoices):
    MALE = ("male","Male")
    FEMALE = ("female","Female")

  class LanguageChoices(models.TextChoices):
    EN = ("english","English")
    KR = ("korea","Korea")

  class CurrencyChoices(models.TextChoices):
    WON = "won","Won"
    DOLLOR = "dollor","Dollor"

  first_name = models.CharField(max_length=150, editable=False)
  last_name =  models.CharField(max_length=150, editable=False)
  name = models.CharField(max_length=150, default="")
  is_host = models.BooleanField(default=False)
  avater = models.ImageField(null=True, blank=True)
  gender = models.CharField(max_length=10,choices=GenderChoices.choices,null=True)
  language = models.CharField(max_length=10,choices=LanguageChoices.choices,null=True)
  currency = models.CharField(max_length=10,choices=CurrencyChoices.choices,null=True)