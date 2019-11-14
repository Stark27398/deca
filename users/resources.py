from import_export import resources, instance_loaders
from users.models import *


def get_instance(self, instance_loader, row):
    try:
        params = {}
        for key in instance_loader.resource.get_import_id_fields():
            field = instance_loader.resource.fields[key]
            params[field.attribute] = field.clean(row)
        return self.get_queryset().get(**params)
    except Exception:
        return None

resources.get_instance = get_instance

# class UploadUser(resources.ModelResource):
#     class Meta:
#         model = User


# class UploadSportsMaster(resources.ModelResource):
#     class Meta:
#         model = SportsMaster


# class uploadEventMaster(resources.ModelResource):
#     class Meta:
#         model = EventMaster


# class UploadClassMaster(resources.ModelResource):
#     class Meta:
#         model = ClassMaster


# class UploadFacilityMaster(resources.ModelResource):
#     class Meta:
#         model = FacilityMaster


# class UploadEventSport(resources.ModelResource):
#     class Meta:
#         model = EventSport


# class UploadClassSport(resources.ModelResource):
#     class Meta:
#         model = ClassSport


# class UploadFacilitySport(resources.ModelResource):
#     class Meta:
#         model = FacilitySport


# class UploadStoreDetails(resources.ModelResource):
#     class Meta:
#         model = StoreDetails


# class UploadTemplates(resources.ModelResource):
#     class Meta:
#         model = Templates


# class UploadSelection(resources.ModelResource):
#     class Meta:
#         model = Selection


