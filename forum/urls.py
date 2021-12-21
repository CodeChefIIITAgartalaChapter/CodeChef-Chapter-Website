from django.urls import path
from . import  views

urlpatterns = [
    path("",views.index,name="home"),
    path("about",views.about,name="about"),
    path("ml",views.ml,name="ml"),
    path("cp",views.CP,name="cp"),
    path("webdev",views.webDev,name="webdev"),
    path("appdev",views.appDev,name="appdev"),
]