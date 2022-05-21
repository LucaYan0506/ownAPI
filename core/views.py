from math import fabs
from re import sub
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import models
from .email import send_feedback_email,send_to_me
import json

# Create your views here.

def index_page(request):
    return HttpResponse("You are in the wrong place, this website is only used for APIs")

@csrf_exempt
def send_message(request):
    if request.method == "POST":
        body = json.loads(request.body)
        name = body['name']
        email = body['email']
        subject = body['subject']
        message = body['message']
        newMessage = models.Message(mail=email, subject=subject, message=message)
        newMessage.save()
        send_feedback_email(email,name)
        send_to_me(email, subject,message, name)
        return JsonResponse("Message sent successfully, thank you for your message. I will reply as soon as possible (make sure that the email is correct, otherwise I cannot reply)",safe=False)
        
    return HttpResponse("Please, send a POST method")