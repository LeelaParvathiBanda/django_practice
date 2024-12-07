from django.db import models

# Create your models here.
class TeamModel(models.Model):
    tname = models.CharField(max_length=50,blank=True)

class PlayerModel(models.Model):
    pname = models.CharField(max_length=60,blank=True)
    ptname = models.CharField(max_length=60,blank=True)
    is_captain = models.BooleanField()