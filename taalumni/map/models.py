from django.db import models

# Create your models here.
class Member(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  company = models.CharField(max_length=50)
  position = models.CharField(max_length=50)
  # location
  city = models.CharField(max_length=60)
  state = models.CharField(max_length=30) # state abbreviation
  # FIXME: image
  email = models.EmailField()
  linkedin = models.URLField(blank=True)

  def __str__(self):
    return "{} {}".format(self.first_name, self.last_name)