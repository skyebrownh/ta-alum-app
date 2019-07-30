from django.shortcuts import render

from .models import Member

def mapView(request):
  num_members = Member.objects.latest('pk').id
  context = {
    'num_members': num_members,
    'members': {},
    'deleted_members': [],
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