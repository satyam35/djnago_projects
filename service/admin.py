from tkinter import S
from django.contrib import admin
from service.models import Service
class ServiceAdmin(admin.ModelAdmin):
    display_field=('service_icon','service_title','service_des','news_image')


from django.contrib.admin.sites import site
site.register(Service,ServiceAdmin)
# Register your models here.
