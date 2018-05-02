from django.shortcuts import render



#takes your request from the app urls page and returns
#either a fuction or class based view (use of render is class based)

def index(request):
    render(request, "Background/home.html")


#this will now send you to the templates folder for the app 
    #where you will return home.html file