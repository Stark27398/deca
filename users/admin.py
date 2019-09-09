from django.contrib import admin
from users.models import User,EventMaster,EventSport,SportsMaster,Templates,Selection
# Register your models here.
admin.site.register(User)
admin.site.register(SportsMaster)
admin.site.register(EventMaster)
admin.site.register(EventSport)
admin.site.register(Templates)
admin.site.register(Selection)