from django.contrib import admin
from contact.models import Contact
# Register your models here.
class AdminContact(admin.ModelAdmin):
    contact_data=('name','email','contact','address')
from django.contrib.admin.sites import site
site.register(Contact,AdminContact)