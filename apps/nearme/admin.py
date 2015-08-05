from django.contrib import admin

from nearme.models import CampusLocation

# Register your models here.

class CampusLocationAdmin(admin.ModelAdmin):
    pass

admin.site.register(CampusLocation, CampusLocationAdmin)
