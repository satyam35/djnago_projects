"""wscubetech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from wscubetech import views


urlpatterns = [
    path('admin/', admin.site.urls,name="admin"),
    path('about-us/', views.aboutUS,name="about"),
    path('', views.homePage,name="home"),
    path('blog/', views.blog,name="blog"),
    path('services/', views.services,name="service"),
    path('contact-us/', views.contact,name="contact"),
    path('pricing/', views.pricing,name="pricing"),
    path('userform/', views.userform),
    path('calculator/', views.calculator,name="cal"),
    path('even-odd/', views.evenodd,name="eo"),
    path('result/', views.result,name="res"),
    path('my_contact/', views.my_contact,name="my_contact"),
    path('newsdetails/<slug:slug>',views.news_details,name='newsdetails'),
    path('submitform/', views.submitform,name="submitform"),
    path('dynamic_url_1/<int:int_data>',views.dynamic_url_int),
    path('dynamic_url_1/<str:string_data>',views.dynamic_url_string),
    path('dynamic_url_1/<slug:slug_data>',views.dynamic_url_slug)
]

if settings.DEBUG :
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)