from django.shortcuts import render

from .models import Member

from google.cloud import storage

def mapView(request):
  # ensure GOOGLE_APPLICATION_CREDENTIALS env variable is set to .json file that holds auth key
  client = storage.Client()
  bucket = client.get_bucket('team-alpha-alumni')
  skye_photo = bucket.get_blob('member_images/Skye.jpg')

  num_members = Member.objects.latest('pk').id
  context = {
    'num_members': num_members,
    'members': {},
    'deleted_members': [],
    'skye_photo': skye_photo.public_url,
  }
  # populate context.members
  for num in range(1, num_members + 1):
    try:
      context["members"]["member_{}".format(num)] = {
        'object': Member.objects.get(pk=num)
      }
    except Member.DoesNotExist:
      context["deleted_members"].append(num)
      continue
  return render(request, 'map/map.html', context)