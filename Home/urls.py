# -*- coding: utf-8 -*-

from django.urls import path
from . import views

urlpatterns=[
        path("admin/", views.index, name="index"),
        path("Home/", views.Home, name="Home")
        ]

