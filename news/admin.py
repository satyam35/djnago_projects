from django.contrib import admin
from news.models import News

class NewNews(admin.ModelAdmin):
   display_field=('headline','news_desc')

from django.contrib.admin.sites import site
site.register(News,NewNews)

# Register your models here.
