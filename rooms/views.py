from django.shortcuts import render
from django.http import HttpResponse
from .models import Room


def see_all_room(request):
  rooms = Room.objects.all()
  return render(request,"all_room.html",{"rooms":rooms , "title":"lalala"})

def see_one_room(request, room_id):
  try:
    room = Room.objects.get(pk=room_id)
    return render(request,"one_room.html",{"room":room})
  except Room.DoesNotExist:
    return render(request,"one_room.html", {"not_found " : True})

