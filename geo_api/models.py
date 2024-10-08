from django.db import models

class Geolocation(models.Model):
    ip_address = models.CharField(max_length=45, unique=True)  # Obsługuje IPv4 i IPv6
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.ip_address} - {self.city}, {self.country}"
