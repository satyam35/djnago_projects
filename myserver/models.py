from django.db import models
class MyServices(models.Model):
    my_icon=models.CharField(max_length=100)
    my_des=models.TextField()
# Create your models here.
