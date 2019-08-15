from django.db import models

import os
import googlemaps

class Member(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  # NOTE: using null on CharField is bad practice. Only use for importing existing data then change back to blank=True instead
  company = models.CharField(max_length=255, blank=True, default='')
  position = models.CharField(max_length=255, blank=True, default='')
  # location
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=50) # state abbreviation
  latitude = models.DecimalField(max_digits=12, decimal_places=7, editable=False)
  longitude = models.DecimalField(max_digits=12, decimal_places=7, editable=False)
  email = models.EmailField(blank=True, null=True)
  linkedin = models.URLField(blank=True, null=True)
  # TODO: image

  def __str__(self):
    return "{} {}".format(self.first_name, self.last_name)

  def save(self):
    # either get city and state from Location DB or geocode and add new entry to Location DB
    try:
      potential_location = Location.objects.get(city=self.city, state=self.state)
      self.latitude = potential_location.latitude
      self.longitude = potential_location.longitude
    except Location.DoesNotExist:
      # geocode this member's city and state
      gmaps = googlemaps.Client(key="{}".format(os.environ.get('GOOGLE_API_KEY')))
      geocode_result = gmaps.geocode("{}, {}".format(self.city, self.state))
      # set lat and long for this member to result of geocode
      self.latitude = geocode_result[0]["geometry"]["location"]["lat"]
      self.longitude = geocode_result[0]["geometry"]["location"]["lng"]
      # create new Location entry
      Location(city=self.city, state=self.state, latitude=self.latitude, longitude=self.longitude).save()
    # call normal save method on this object
    super(Member, self).save()


class Location(models.Model):
  # DB starts empty and gets populated as Members are added
  city = models.CharField(max_length=60)
  state = models.CharField(max_length=30)
  latitude = models.DecimalField(max_digits=12, decimal_places=7, editable=False)
  longitude = models.DecimalField(max_digits=12, decimal_places=7, editable=False)

  def __str__(self):
    return "{}, {}: {}, {}".format(self.city, self.state, self.latitude, self.longitude)