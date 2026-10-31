
import requests

BASE_URL = "http://127.0.0.1:3000"
endpoint = "/rest/products/search"

try:
    response = requests.get(
        BASE_URL + endpoint,
        params={"q": "banana"},
        timeout=10
    )

    print(f"HTTP Status: {response.status_code}")

    response.raise_for_status()
    data = response.json()

    products = data.get("data", [])

    print(f"Products found: {len(products)}")

    for product in products:
        print(f"Product ID: {product['id']}")
        print(f"Name: {product['name']}")
        print(f"Price: {product['price']}")

except requests.RequestException as error:
    print(f"Request failed: {error}")
except (ValueError, KeyError, TypeError) as error:
    print(f"Unexpected response data: {error}")
