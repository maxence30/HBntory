from product_api import list_products as api_list_products
from product_api import get_product as api_get_product


def list_available_products():

    return api_list_products()



def retrieve_product(product_id: int):

    return api_get_product(product_id)