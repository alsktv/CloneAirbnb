from rest_framework.test import APITestCase

class TestAmenties(APITestCase):

  def test_all_amenities(self):

     response= self.client.get("api/v1/rooms/amentities")
     data = response.json()

     self.assertEqual(
        response.status_code,200,"status code isn't 200",
     )
    
