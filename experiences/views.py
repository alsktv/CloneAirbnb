from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_204_NO_CONTENT
from .serializers import PerkSerializer
from .models import Perk

class Perks(APIView):

  def get(self,request):
    perks = Perk.objects.all()
    return Response(PerkSerializer(perks , many = True).data)

  def post(self,request):
    serializer = PerkSerializer(data = request.data)
    if serializer.is_valid():
      created_data = serializer.save()
      return Response(PerkSerializer(created_data).data)
    else: return Response(serializer.errors)

class PerkDetail(APIView):

  def get_object(self,pk):
    try:
      return Perk.objects.get(pk = pk)
    except Perk.DoesNotExist:
      raise NotFound
      

  def get(self,request,pk):
    perk = self.get_object(pk)
    serializer = PerkSerializer(perk)
    return Response(serializer.data)

  def put(self,request,pk):
    perk = self.get_object(pk)
    serializer = PerkSerializer(perk,data = request.data , partial = True)
    if serializer.is_valid():
      updated_data = serializer.save()
      return Response(PerkSerializer(updated_data).data)
    else: return Response(serializer.errors)

  def delete(self,request,pk):
    perk = self.get_object(pk)
    perk.delete()
    return Response(status =  HTTP_204_NO_CONTENT)
