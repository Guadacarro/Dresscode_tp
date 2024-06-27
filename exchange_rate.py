import requests


def get_xr():
    url = "https://api.bluelytics.com.ar/v2/latest"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['oficial']['value_sell']
    else:
        print("Failed to fetch data:", response.status_code)
        return None