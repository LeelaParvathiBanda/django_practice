from django.db import models

# Create your models here.
class TeamModel(models.Model):
    t_name = models.CharField(max_length = 50,blank = True)
class playerModel(models.Model):
    pname = models.CharField(max_length = 50,blank = True)
    ptname = models.CharField(max_length=50,blank=True)
    is_captain = models.BooleanField()

