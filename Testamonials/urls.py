from django.urls import path
from . import views

urlpatterns=[
        path("Testamonials/", views.index, name="Testamonials"),
        ]