from rest_framework import status, views
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Geolocation
from .serializers import GeolocationSerializer
from .services import get_geolocation_data

class GeolocationView(views.APIView):

    def get(self, request: Request, ip_or_url: str) -> Response:
        geolocation = get_object_or_404(Geolocation, ip_address=ip_or_url)
        serializer = GeolocationSerializer(geolocation)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        if not (ip_or_url := request.data.get("ip_or_url")):
            return Response({"error": "IP or URL required."}, status=status.HTTP_400_BAD_REQUEST)

        if geolocation_data := get_geolocation_data(ip_or_url):
            geolocation, created = Geolocation.objects.get_or_create(ip_address=ip_or_url, defaults=geolocation_data)
            serializer = GeolocationSerializer(geolocation)
            return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)

        return Response({"error": "Invalid IP or URL."}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, ip_or_url: str) -> Response:
        geolocation = get_object_or_404(Geolocation, ip_address=ip_or_url)
        geolocation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
