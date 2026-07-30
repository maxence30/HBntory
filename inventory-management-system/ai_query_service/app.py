from flask import Flask, request, jsonify

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from agent.query_agent import root_agent

from tools.stock_tools import (
    get_total_stock,
    get_product_stock,
    get_branch_stock
)

import asyncio
import re


app = Flask(__name__)


session_service = InMemorySessionService()

runner = Runner(
    agent=root_agent,
    app_name="HBntory",
    session_service=session_service
)


@app.route("/query", methods=["POST"])
def query():

    data = request.json

    question = data.get("question")

    if not question:
        return jsonify({
            "error": "Question required"
        }), 400


    question_lower = question.lower()


    # TOTAL STOCK
    if (
        "combien" in question_lower
        and "stock" in question_lower
    ) or "total stock" in question_lower:

        result = get_total_stock()

        return jsonify({
            "answer": f"Nous avons actuellement {result['total_stock']} produits en stock."
        })


    # STOCK PRODUIT
    if "produit" in question_lower:

        match = re.search(r"\d+", question)

        if match:

            product_id = int(match.group())

            result = get_product_stock(product_id)

            if result:

                return jsonify({
                    "answer": f"Stock du produit {product_id}: {result}"
                })

            return jsonify({
                "answer": "Aucun stock trouvé pour ce produit."
            })


    # STOCK BRANCHE
    if "branche" in question_lower:

        match = re.search(r"\d+", question)

        if match:

            branch_id = int(match.group())

            result = get_branch_stock(branch_id)

            if result:

                return jsonify({
                    "answer": f"Stock de la branche {branch_id}: {result}"
                })

            return jsonify({
                "answer": "Aucun stock trouvé pour cette branche."
            })


    # QUESTIONS IA NORMALES
    async def run_agent():

        session = await session_service.create_session(
            app_name="HBntory",
            user_id="user"
        )


        content = types.Content(
            role="user",
            parts=[
                types.Part(
                    text=question
                )
            ]
        )


        answer = ""


        async for event in runner.run_async(
            user_id="user",
            session_id=session.id,
            new_message=content
        ):

            if event.content and event.content.parts:

                for part in event.content.parts:

                    if part.text:
                        answer += part.text


        return answer


    result = asyncio.run(run_agent())


    return jsonify({
        "answer": result
    })


if __name__ == "__main__":

    app.run(
        port=7000,
        debug=True
    )