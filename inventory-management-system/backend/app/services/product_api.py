import requests
import os


PRODUCT_API_URL = os.getenv(
    "PRODUCT_API_URL",
    "http://localhost:8000"
)


def get_products():

    try:
        response = requests.get(
            f"{PRODUCT_API_URL}/products"
        )

        if response.status_code != 200:
            return {
                "error": "Product API unavailable"
            }

        return response.json()

    except requests.exceptions.RequestException:

        return {
            "error": "Cannot connect to Product API"
        }



def get_product(product_id):

    try:
        response = requests.get(
            f"{PRODUCT_API_URL}/products/{product_id}"
        )

        if response.status_code == 404:
            return {
                "error": "Product not found"
            }

        if response.status_code != 200:
            return {
                "error": "Product API unavailable"
            }

        return response.json()


    except requests.exceptions.RequestException:

        return {
            "error": "Cannot connect to Product API"
        }