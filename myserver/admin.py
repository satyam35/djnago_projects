from django.contrib import admin
from myserver.models import MyServices
class Server(admin.ModelAdmin):
    ser=('my_icon','my_des')

from django.contrib.admin.sites import site
site.register(MyServices,Server)
    
# Register your models here.
