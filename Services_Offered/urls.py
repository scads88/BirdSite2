from django.urls import path
from . import views

urlpatterns=[
        path("Services_Offered/", views.index, name="Services_Offered")
        ]