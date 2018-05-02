# -*- coding: utf-8 -*-

from django.urls import path
from . import views

urlpatterns=[
        path("Background/", views.index, name="Background"),
        ]

