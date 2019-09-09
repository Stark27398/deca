from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(max_length=254)
    userid = models.CharField(max_length=100)

    def __str__(self):
        return self.email

class SportsMaster(models.Model):
    uuid = models.CharField(max_length=100)
    sportsname = models.CharField(max_length=100)

    def __str__(self):
        return self.sportsname

class EventMaster(models.Model):
    uuid = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    lat = models.FloatField()
    lng = models.FloatField()
    minPrice = models.IntegerField()
    maxPrice = models.IntegerField()
    startDate = models.DateField(auto_now=False, auto_now_add=False)
    starttime = models.TimeField(auto_now=False, auto_now_add=False)
    endDate = models.DateField(auto_now=False, auto_now_add=False)
    endtime = models.TimeField(auto_now=False, auto_now_add=False)
    isPublished = models.BooleanField()
    isDisabled = models.BooleanField()
    isDeleted = models.BooleanField()
    isActive = models.BooleanField()

    def __str__(self):
        return self.uuid
    

class EventSport(models.Model):
    eventId = models.CharField(max_length=100)
    sportsId = models.CharField(max_length=100)
    
class Templates(models.Model):
    typeof = models.CharField(max_length=20)
    sportbtn = models.TextField()
    location = models.TextField()
    userid = models.TextField()
    submit = models.TextField()

class Selection(models.Model):
    name = models.CharField(max_length=50)
    sportbtn = models.BooleanField()
    location = models.BooleanField()
    userid = models.BooleanField()
    url = models.TextField()
    endpoint = models.CharField(max_length=200,default="")

    def __str__(self):
        return self.name
    
