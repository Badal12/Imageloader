from django.db import models

# Create your models here.
class Image(models.Model): #here it created the image table in db
    photo = models.ImageField(upload_to="myimage") #upload to indicate and create the new folder the where our images going to store
    date = models.DateTimeField(auto_now_add = True)