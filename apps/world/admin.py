from django.contrib.gis import admin

from leaflet.admin import LeafletGeoAdmin

from world.models import WorldBorder

# admin.site.register(WorldBorder, admin.GeoModelAdmin)
admin.site.register(WorldBorder, LeafletGeoAdmin)
