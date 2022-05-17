from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import models

# Create your views here.

def index_page(request):
    return HttpResponse("You are in the wrong place, this website is only used for APIs")

@csrf_exempt
def send_message(request):
    if request.method == "POST":
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        newMessage = models.Message(mail=email, subject=subject, message=message)
        newMessage.save()
        
    return HttpResponse("Please, send a POST method")