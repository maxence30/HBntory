import asyncio

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from agent.query_agent import root_agent


async def main():

    session_service = InMemorySessionService()

    runner = Runner(
        agent=root_agent,
        app_name="HBntory",
        session_service=session_service
    )

    session = await session_service.create_session(
        app_name="HBntory",
        user_id="test"
    )

    message = types.Content(
        role="user",
        parts=[
            types.Part(
                text="Where is product 1 available?"
            )
        ]
    )

    async for event in runner.run_async(
        user_id="test",
        session_id=session.id,
        new_message=message
    ):

        if event.content:
            print(event.content)


asyncio.run(main())
