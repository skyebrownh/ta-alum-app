from django.shortcuts import render

from google.cloud import storage

def landingPage(request):
  client = storage.Client()
  bucket = client.get_bucket('team-alpha-alumni')
  skye_photo = bucket.get_blob('member_images/Skye.jpg')

  return render(request, 'home/landing-page.html', {'skye_photo': skye_photo.public_url})