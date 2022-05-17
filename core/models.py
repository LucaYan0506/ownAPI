from django.db import models
from ckeditor.fields import RichTextField 

# Create your models here.
class Message(models.Model):
    mail = models.EmailField(max_length=254)
    subject = models.TextField(max_length=254)
    message = RichTextField()