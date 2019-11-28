from django.contrib import admin
# from users.models import *
from django.apps import apps


models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
# Register your models here.

# admin.site.register(User)
# admin.site.register(SportsMaster)
# admin.site.register(EventMaster)
# admin.site.register(EventSport)
# admin.site.register(Templates)
# admin.site.register(Selection)
# admin.site.register(ClassMaster)
# admin.site.register(ClassSport)
# admin.site.register(FacilityMaster)
# admin.site.register(FacilitySport)
# admin.site.register(contentId)
# admin.site.register(StoreDetails)


# @admin.register(User)
# class UploadUser(ImportExportModelAdmin):
#     pass


# @admin.register(SportsMaster)
# class UploadSportsMaster(ImportExportModelAdmin):
#     pass


# @admin.register(EventMaster)
# class UploadEventMaster(ImportExportModelAdmin):
#     pass


# @admin.register(EventSport)
# class UploadEventSport(ImportExportModelAdmin):
#     pass


# @admin.register(Templates)
# class UploadTemplates(ImportExportModelAdmin):
#     pass


# @admin.register(Selection)
# class UploadSelection(ImportExportModelAdmin):
#     pass


# @admin.register(ClassMaster)
# class UploadClassMaster(ImportExportModelAdmin):
#     pass


# @admin.register(ClassSport)
# class UploadClassSport(ImportExportModelAdmin):
#     pass


# @admin.register(FacilityMaster)
# class UploadFacilityMaster(ImportExportModelAdmin):
#     pass


# @admin.register(FacilitySport)
# class UploadFacilitySport(ImportExportModelAdmin):
#     pass


# @admin.register(StoreDetails)
# class UploadStoreDetails(ImportExportModelAdmin):
#     pass
