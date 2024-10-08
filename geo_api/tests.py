from django.test import TestCase
from rest_framework.test import APIClient
from .models import Geolocation

class GeolocationAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_add_geolocation(self):
        # Test dodania geolokalizacji dla IP 192.168.0.1
        response = self.client.post('/api/geolocation/', {"ip_or_url": "7.7.7.7"})
        self.assertEqual(response.status_code, 201)

    def test_get_geolocation(self):
        Geolocation.objects.create(
            ip_address="7.7.7.7",
            city="Ashburn",
            country="USA",
            latitude=39.043701171875,
            longitude=-77.47419738769531
        )
        response = self.client.get('/api/geolocation/7.7.7.7/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['city'], "Ashburn")

    def test_delete_geolocation(self):
        Geolocation.objects.create(
            ip_address="192.168.0.1",
            city="Los Angeles",
            country="USA",
            latitude=34.0522,
            longitude=-118.2437
        )
        response = self.client.delete('/api/geolocation/192.168.0.1/')
        self.assertEqual(response.status_code, 204)

