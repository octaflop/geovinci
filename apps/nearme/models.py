# from django.db import models
from django.contrib.gis.db import models


class CampusLocation(models.Model):
    """
    A general location of the campus
    """
    street_address = models.CharField(max_length=240)
    additional_address = models.CharField(
        max_length=240, blank=True, help_text="Apartment or Suite Number")
    locality = models.CharField(
        help_text="The city or municipality of the campus", max_length=240)
    region = models.CharField(
        help_text="State or Province of the campus (Abbreviation preffered)", max_length=100)
    telephone = models.CharField(
        help_text="Phone number of the campus", max_length=50, blank=True)
    zip_code = models.CharField(
        help_text="Zip or Postal Code of the campus", max_length=10, blank=True)

    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    point = models.PointField(blank=True, null=True)

    objects = models.GeoManager()

    def __str__(self):
        return "{0} \n {1}, {2}".format(self.street_address, self.locality, self.region)

    def save(self, *args, **kwargs):
        if self.point is None:
            from haystack.utils.geo import Point
            if self.lon is not None and self.lat is not None:
                self.point = Point(self.lon, self.lat)
            elif self.full_address != "":
                try:
                    from geopy.geocoders import GoogleV3
                    geolocator = GoogleV3()
                    try:
                        lat, lon = geolocator.geocode(self.full_address)[1]
                        self.lat = lat
                        self.lon = lon
                        self.point = Point(lon, lat)
                    except IndexError:
                        pass
                except Exception:
                    pass

            # TODO: else with the street address and geo encoder via google or something
        super(CampusLocation, self).save(*args, **kwargs)

    @property
    def full_address(self):
        ctx = {
            'street_address': self.street_address,
            'additional_address': self.additional_address,
            'locality': self.locality,
            'region': self.region,
            'zip_code': self.zip_code,
        }
        full_address = """
        {street_address} {additional_address}, {locality}, {region}, {zip_code}
        """.format(**ctx)
        return full_address
