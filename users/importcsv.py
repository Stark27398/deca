from csvImporter.model import CsvModel
from users.models import *

class UploadUser(CsvModel):
    email = EmailField()
    userid = CharField()

    class Meta:
        delimiter = ";"
        dbModel = User


class UploadSportsMaster(CsvModel):
    uuid = CharField()
    sportsname = CharField()

    class Meta:
        delimiter = ";"
        dbModel = SportsMaster


class uploadEventMaster(CsvModel):
    uuid = CharField()
    name = CharField()
    businessId = CharField()
    lat = FloatField()
    lng = FloatField()
    minPrice = IntegerField()
    maxPrice = IntegerField()
    startDate = DateField()
    starttime = TimeField()
    endDate = DateField()
    endtime = TimeField()
    isPublished = BooleanField()
    isDisabled = BooleanField()
    isDeleted = BooleanField()
    isActive = BooleanField()

    class Meta:
        delimiter = ";"
        dbModel = EventMaster


class UploadClassMaster(CsvModel):
    uuid = CharField()
    name = CharField()
    businessId = CharField()
    lat = FloatField()
    lng = FloatField()
    price = IntegerField()
    isPublished = BooleanField()
    isDisabled = BooleanField()
    isDeleted = BooleanField()
    isActive = BooleanField()

    class Meta:
        delimiter = ";"
        dbModel = ClassMaster


class UploadFacilityMaster(CsvModel):
    uuid = CharField()
    name = CharField()
    businessId = CharField()
    minPrice = IntegerField()
    maxPrice = IntegerField()
    lat = FloatField()
    lng = FloatField()

    class Meta:
        delimiter = ";"
        dbModel = FacilityMaster


class UploadEventSport(CsvModel):
    eventId = CharField()
    sportsId = CharField()

    class Meta:
        delimiter = ";"
        dbModel = EventSport


class UploadClassSport(CsvModel):
    eventId = CharField()
    sportsId = CharField()

    class Meta:
        delimiter = ";"
        dbModel = ClassSport


class UploadFacilitySport(CsvModel):
    eventId = CharField()
    sportsId = CharField()

    class Meta:
        delimiter = ";"
        dbModel = FacilitySport


class UploadStoreDetails(CsvModel):
    storeId = CharField()
    name = CharField()

    class Meta:
        delimiter = ";"
        dbModel = StoreDetails


class UploadTemplates(CsvModel):
    typeof = CharField()
    sportbtn = TextField()
    location = TextField()
    userid = TextField()
    submit = TextField()

    class Meta:
        delimiter = ";"
        dbModel = Templates


class UploadSelection(CsvModel):
    name = CharField()
    keyId = CharField()
    sportbtn = BooleanField()
    location = BooleanField()
    userid = BooleanField()
    url = TextField()
    endpoint = CharField()

    class Meta:
        delimiter = ";"
        dbModel = Selection
