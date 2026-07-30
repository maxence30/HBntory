from mcp.server.fastmcp import FastMCP

from tools import (
    list_available_products,
    retrieve_product
)


app = FastMCP(
    "Product MCP Server"
)


@app.tool()
def list_products():

    """
    Return all available products.
    """

    return list_available_products()


@app.tool()
def get_product(product_id: int):

    """
    Retrieve a product by id.
    """

    return retrieve_product(product_id)


if __name__ == "__main__":

    app.run()