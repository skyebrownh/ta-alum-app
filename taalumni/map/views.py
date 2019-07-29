from django.shortcuts import render

from .models import Member

def mapView(request):
  num_members = Member.objects.count()
  context = {
    'num_members': num_members,
    'members': {},
  }
  # populate context.members
  for num in range(1, num_members + 1):
    context["members"]["member_{}".format(num)] = {
      'object': Member.objects.get(pk=num)
    }
  return render(request, 'map/map.html', context)