import requests


PRODUCT_API_URL = "http://127.0.0.1:8000/products"



def list_products():

    try:

        response = requests.get(
            PRODUCT_API_URL
        )

        response.raise_for_status()

        return response.json()


    except requests.exceptions.RequestException as error:

        raise Exception(
            f"Product API connection error: {error}"
        )



def get_product(product_id: int):

    try:

        response = requests.get(
            f"{PRODUCT_API_URL}/{product_id}"
        )


        if response.status_code == 404:

            return None


        response.raise_for_status()

        return response.json()


    except requests.exceptions.RequestException as error:

        raise Exception(
            f"Product API connection error: {error}"
        )