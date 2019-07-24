from django.shortcuts import render

from .models import Member

import googlemaps
from .constants import API_KEY

def mapView(request):
  num_members = Member.objects.count()
  context = {
    'num_members': num_members,
    'members': {},
  }
  # send converted city, state to lat, long with member_<num>
  gmaps = googlemaps.Client(key="{}".format(API_KEY))
  # populate context.members
  for num in range(1, num_members + 1):
    geocode_result = gmaps.geocode("{}, {}".format(Member.objects.get(pk=num).city, Member.objects.get(pk=num).state))
    context["members"]["member_{}".format(num)] = {
      'object': Member.objects.get(pk=num),
      'lat': geocode_result[0]["geometry"]["location"]["lat"],
      'long': geocode_result[0]["geometry"]["location"]["lng"]
    }
  return render(request, 'map/map.html', context)