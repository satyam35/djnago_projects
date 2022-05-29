from email.policy import default
from enum import unique
from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField
# Create your models here.
class News(models.Model):
    headline=models.CharField(max_length=50)
    news_desc=HTMLField()
    news_image=models.ImageField(upload_to="news/",max_length=400,null=True,default=None)
    new_slug=AutoSlugField(populate_from='headline',unique=True,null=True,default=None)