from django.shortcuts import render


def index(request):
    return render(request, "Services_Offered/home.html")
# Create your views here.
