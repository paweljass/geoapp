from django.urls import path
from geo_api.views import GeolocationView

urlpatterns = [
    path('api/geolocation/<str:ip_or_url>/', GeolocationView.as_view()),
    path('api/geolocation/', GeolocationView.as_view()),
]

