from django.urls import path
from myapp import views

urlpatterns = [
    path("", views.home, name="home"),
    path("myapp/<name>", views.test, name="test"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),

]