from tools.stock_tools import get_product_stock
from tools.product_tools import get_product_tools


async def answer_product_location(product_id: int):
    """
    Return where a product is available using MCP tools.
    """

    tools = await get_product_tools()

    available_tools = [
        tool.name
        for tool in tools.tools
    ]

    if "get_product" not in available_tools:
        return {
            "error": "Product MCP tool unavailable"
        }

    stock = get_product_stock(product_id)

    if not stock:
        return {
            "message": "No stock available"
        }

    return {
        "product_id": product_id,
        "available_at": stock
    }


async def generate_answer(product_id: int):
    """
    Generate a user-friendly answer from product availability data.
    """

    result = await answer_product_location(product_id)

    if "error" in result:
        return result["error"]

    if "message" in result:
        return result["message"]

    locations = []

    for item in result["available_at"]:
        locations.append(
            f"{item['branch']} ({item['quantity']} units)"
        )

    return (
        f"Product {product_id} is available at: "
        + ", ".join(locations)
    )