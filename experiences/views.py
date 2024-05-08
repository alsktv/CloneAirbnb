from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound,ParseError
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.permissions import IsAuthenticated
from .serializers import PerkSerializer,TinyExperienceSerializer,ExperienceSerializer
from .models import Perk,Experience
from books.serializers import PublicBookingSerializer,CreateExperienceBookingSerializer,ExperienceBookDetailSerializer
from books.models import Book

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

class Experiences(APIView):

  def get(self,request):
    
    try:
      experiences = Experience.objects.all()
      page = int(request.query_params.get("page",1)) #query_params이용하여 params가져올 수 있음(dict)
      page_width = 5
      serializer = TinyExperienceSerializer(experiences[(page-1)*page_width   : (page)*page_width ],many = True)
      return Response(serializer.data)
    except ValueError: #올바르지 못한 값 입력에 대한 예외처리
      page = 1
  
  def post(self,request):
    serializer = ExperienceSerializer(data = request.data)
    if serializer.is_valid():
      created_data = serializer.save()
      return Response(ExperienceSerializer(created_data).data)
    else:
      return Response(serializer.errors)
    
class ExperienceDetail(APIView):
  def get_objects(self,pk):
     try:
      return Experience.objects.get(pk = pk)
     except Experience.DoesNotExist:
       return NotFound

  def get(self,request,pk):
    experience = self.get_objects(pk)
    serializer = ExperienceSerializer(experience)
    return Response(serializer.data)
  
  def put(self,request,pk):
    experience = self.get_objects(pk)
    serializer = ExperienceSerializer(experience, data= request.data , partial = True)
    if serializer.is_valid():
      updated_data = serializer.save()
      return Response(ExperienceSerializer(updated_data).data)
    else:
      return ParseError()
    
  def delete(self,request,pk):
    experience = self.get_objects(pk)
    experience.delete()
    return Response(status =  HTTP_204_NO_CONTENT)
    
class ExperiencePerk(APIView):
  def get(self,request,pk):
    try:
      experience = Experience.objects.get(pk = pk)
      perks = experience.perk
      serializer = PerkSerializer(perks , many = True)
      return Response(serializer.data)
    except Experience.DoesNotExist:
      raise NotFound
    
# 하나의 experience에 있는 bookings을 전부 가져옴
class Bookings(APIView):  
  permission_classes = [IsAuthenticated]
  def get_object(self,pk):
    try:
      return Experience.objects.get(pk = pk)
    except Experience.DoesNotExist:
      raise NotFound
    
  def get(self,request,pk):
    experience = self.get_object(pk)
    bookings = experience.books
    return Response( CreateExperienceBookingSerializer(bookings, many = True).data)
  
  def post(self,request,pk):
    serializer = CreateExperienceBookingSerializer(data = request.data)
    if serializer.is_valid():
      created_data = serializer.save(
        user = request.user,
        experience = self.get_object(pk),
        kind = Book.BookKindChoices.EXPERIENCE,
      )
      return Response(CreateExperienceBookingSerializer(created_data).data)
    else:
      return Response(serializer.errors)

class BookDetail(APIView):
  permission_classes = [IsAuthenticated]
  def get_objects(self,pk,bookPk):
    try:
      experience = Experience.objects.get(pk = pk)
      book = experience.books.all()[bookPk-1]  #여러개의 book중 선택 ##queryset에서 list문법 사용하고 싶으면 all()을 해줘야함. 왜냐하면 queryset은 related manager중 하나이기 때문이다.
      return book
    except Experience.DoesNotExist or not book:
      raise NotFound
    
  def get(self,request,pk,bookPk):
    book = self.get_objects(pk,bookPk)
    serializer = ExperienceBookDetailSerializer(book)
    return Response(serializer.data)
  
  def put(self,request,pk,bookPk):
    book = self.get_objects(pk,bookPk)
    if book.user != request.user:
      raise ParseError("You didn't have permission to change.")
    else:
      serializer = ExperienceBookDetailSerializer(book,data = request.data , partial = True)
      if serializer.is_valid():
        updated_data = serializer.save(
          user = request.user
        )
        return Response(ExperienceBookDetailSerializer(updated_data).data)
      else:
        return Response(serializer.errors)
      
  def delete(self,request,pk,bookPk):
    book = self.get_objects(pk,bookPk)
    if request.user == book.user:
      book.delete()
      return Response({"status": "delete is successful"})
    else:
      raise ParseError("You don't have permission to delete")
    
      