from flask import Flask, jsonify

app = Flask(__name__)


products = [
    {
        "id": 1,
        "name": "Laptop",
        "category": "Computer",
        "price": 999
    },
    {
        "id": 2,
        "name": "Mouse",
        "category": "Accessory",
        "price": 30
    },
    {
        "id": 3,
        "name": "Keyboard",
        "category": "Accessory",
        "price": 80
    }
]


@app.route("/products", methods=["GET"])
def list_products():
    return jsonify(products)


@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):

    for product in products:

        if product["id"] == product_id:
            return jsonify(product)

    return jsonify({
        "message": "Product not found"
    }), 404


if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=8000,
        debug=True
    )