from rest_framework.views import APIView
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.response import Response
from rest_framework.exceptions import NotFound,NotAuthenticated,PermissionDenied
from rest_framework.permissions import IsAuthenticated
from .models import Photo

class PhotoDetail(APIView):

  permission_classes = [IsAuthenticated] #이렇게 해 주면 일일히 if,else 칠 필요 없음

  def get_objects(self,pk):
    try:
         photo = Photo.objects.get(pk = pk)
         return photo
    except Photo.DoesNotExist:
       raise NotFound
  def delete(self,request,pk):
    photo = self.get_objects(pk)
    if request.user.is_authenticated:
       raise NotAuthenticated
    if photo.room: #photo.room 은 foreignkey인대, 여기서는 인스턴스임(related_name으로 가져온것은 쿼리셋임).따라서 인스턴스의 속성값들도 가져올 수 있음
       if photo.room.owner != request.user: #이것도 둘다 인스턴스임
          raise PermissionDenied
    elif photo.experience:
      if photo.experience.host != request.owner:
         raise PermissionDenied
          
    photo.delete()
    return Response(status = HTTP_204_NO_CONTENT)
  
