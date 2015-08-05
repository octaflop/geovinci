from django.shortcuts import render
from django.contrib.gis.geoip import GeoIP
from django.contrib.gis.geos import Point

from nearme.models import CampusLocation

def coarse(request):
    ctx = {}
    ctx['demo'] = "coarse"
    template_name = "nearme/front/index.html"

    ip_addr = request.META['REMOTE_ADDR']
    print("Actual IP: {0}".format(ip_addr))
    # Faked IP based on Zaniac Sugar House
    FAKED_IP = "50.77.46.89"
    ip_addr = FAKED_IP

    ctx['ip'] = ip_addr
    g = GeoIP()
    ctx['city'] = g.city(ip_addr)

    return render(request, template_name, ctx)


def fine(request):
    ctx = {}
    ctx['demo'] = "fine"
    template_name = "nearme/front/index.html"

    return render(request, template_name, ctx)


def campuses(request):
    ctx = {}
    ctx['marker'] = {}
    ctx['demo'] = "campuses"
    template_name = "nearme/front/campuses.html"

    print(request.GET)
    lat, lng = request.GET.get('lat', None), request.GET.get('lng', None)
    if lat is not None and lng is not None:
        ctx['marker']['lat'], ctx['marker']['lng'] = lat, lng

    query_method = request.GET.get('qmethod', 'geodjango')
    ctx['qmethod'] = query_method

    if lat is not None and lng is not None:
        qmethod = query_method.lower()
        if qmethod == "geodjango":
            ref_location = Point(float(lng), float(lat))  # because x, y
            campus_locations = CampusLocation.objects.all().distance(ref_location).order_by('distance')
            ctx['campus_locations'] = campus_locations

    return render(request, template_name, ctx)
