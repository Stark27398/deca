from django.db import models

# Create your models here.
class contentId(models.Model):
    typeId = models.IntegerField(primary_key=True)
    classtype = models.CharField(max_length=100,default="")
    name = models.CharField(max_length=100)
    sport = models.CharField(max_length=100 )
    def __str__(self):
        return self.name
    
class User(models.Model):
    email = models.EmailField(max_length=254)
    userid = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.email

class SportsMaster(models.Model):
    uuid = models.CharField(max_length=100, primary_key=True)
    sportsname = models.CharField(max_length=100)
    group = models.CharField(max_length=200)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.sportsname

class EventMaster(models.Model):
    uuid = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=200)
    businessId = models.CharField(max_length=100)
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


class ClassMaster(models.Model):
    uuid = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=200)
    businessId = models.CharField(max_length=100)
    minPrice = models.FloatField()
    isPublished = models.BooleanField()
    isDisabled = models.BooleanField()
    isDeleted = models.BooleanField()
    isActive = models.BooleanField()

    def __str__(self):
        return self.uuid


class FacilityMaster(models.Model):
    uuid = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=200)
    businessId = models.CharField(max_length=100)
    minPrice = models.FloatField(default=0,null=True)
    maxPrice = models.FloatField(default=0,null=True)
    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        return self.uuid
    

class EventSport(models.Model):
    id = models.AutoField(primary_key=True)
    eventId = models.CharField(max_length=100)
    sportsId = models.CharField(max_length=100)
    tf = models.BooleanField(default=True)

class ClassSport(models.Model):
    id = models.AutoField(primary_key=True)
    eventId = models.CharField(max_length=100)
    sportsId = models.CharField(max_length=100)
    tf = models.BooleanField(default=True)

class FacilitySport(models.Model):
    id=models.AutoField(primary_key=True)
    eventId = models.CharField(max_length=100)
    sportsId = models.CharField(max_length=100)
    tf = models.BooleanField(default=True)

class StoreDetails(models.Model):
    storeId = models.CharField(max_length=100,primary_key=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    

class Templates(models.Model):
    id = models.IntegerField(primary_key=True)
    typeof = models.CharField(max_length=20)
    sportbtn = models.TextField()
    location = models.TextField()
    userid = models.TextField()
    submit = models.TextField()

class Selection(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    keyId = models.CharField(max_length=100)
    sportbtn = models.BooleanField()
    location = models.BooleanField()
    userid = models.BooleanField()
    url = models.TextField()
    endpoint = models.CharField(max_length=200,default="")
    notAvailable = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
