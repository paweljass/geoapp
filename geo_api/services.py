import requests
from typing import Dict, Optional

# move API_KEY to env in production
API_KEY = '206312e2bcd573e087536bf360ec07c6'
BASE_URL = 'http://api.ipstack.com/'


def get_geolocation_data(ip_or_url: str) -> Optional[Dict]:
    url = f"{BASE_URL}{ip_or_url}?access_key={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data.get("latitude") and data.get("longitude"):
            return {
                "city": data.get("city"),
                "country": data.get("country_name"),
                "latitude": data.get("latitude"),
                "longitude": data.get("longitude"),
            }
    return None
