from rest_framework.test import APITestCase
from django.urls import reverse
from rooms.models import Amenity

class TestAmenties(APITestCase):
  
  NAME = "Amenity test" #계속 사용하기 위해서 property로 만듬
  DESC = "Amenity test"
  
  def setUp(self):
    Amenity.objects.create(
      name = self.NAME,
      description = self.DESC,
    )  #이렇게 하면 비어있던 가상에 모델에 인스턴스가 추가됨

  def test_all_amenities(self):
   response =  self.client.get(reverse("amenities")) #이러면 get으로 request를 보내줌,reverse로 하니까 됨. 이걸로 response가 내가 의도한 대로 오고 있는지 확인 가능함.**
   data = response.json()

   self.assertEqual(response.status_code,200,"Status code isn't 200") #self에 있는 method로 test해주는 것임

   self.assertIsInstance(data, list , "data는 리스트 여야 함")  #get으로 받은 값이 list인지를 확인함

   self.assertEqual(len(data),1)
   self.assertEqual(data[0].get("name") , self.NAME)
   self.assertEqual(data[0].get("description") , self.DESC)

  def  test_create_amenities(self):
    
    response = self.client.post(reverse("amenities") , data = {
      "name":"jump",
      "description": "more jump more health!",
    })

    data = response.json()

    self.assertEqual(response.status_code,200,"Not 200 status code")
