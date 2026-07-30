from flask import Flask, request, jsonify
import asyncio

from agent.query_agent import generate_answer


app = Flask(__name__)


@app.route("/query", methods=["POST"])
def query():

    data = request.json

    product_id = data.get("product_id")

    if not product_id:
        return jsonify({
            "error": "product_id is required"
        }), 400

    answer = asyncio.run(
        generate_answer(product_id)
    )

    return jsonify({
        "answer": answer
    })


if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=7000,
        debug=True
    )
