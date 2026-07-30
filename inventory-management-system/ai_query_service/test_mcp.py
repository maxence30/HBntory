import asyncio

from tools.product_tools import get_product_tools


async def main():

    tools = await get_product_tools()

    for tool in tools.tools:
        print(tool.name)


asyncio.run(main())
