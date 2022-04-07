from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.home , name="home"),
    path("gallery", views.gallery , name="gallery"),
    path("blog", views.blog , name="blog"),
    path("about", views.about , name="about"),
    path("contact", views.contact , name="contact"),
    path("menu", views.menu , name="menu"),
    path("service", views.services, name="services"),
    
    

]