from mcp.client.session import ClientSession
from mcp.client.stdio import stdio_client, StdioServerParameters


async def get_product_tools():

    server_params = StdioServerParameters(
        command="python",
        args=[
            "../product_mcp_server/server.py"
        ]
    )

    async with stdio_client(
        server_params
    ) as (read, write):

        async with ClientSession(
            read,
            write
        ) as session:

            await session.initialize()

            tools = await session.list_tools()

            return tools
