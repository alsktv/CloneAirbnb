from django.db import models

class CommonModel(models.Model):
  """common Model definition"""
  created_at = models.DateTimeField(auto_now_add=True,null=True)
  updated_at = models.DateTimeField(auto_now=True,null=True)

  class Meta:
    abstract = True