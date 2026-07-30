from flask import Blueprint, request, session, jsonify

from app.database import SessionLocal
from app.models.stock import Stock

stock_bp = Blueprint("stock", __name__)


def check_common_user():

    if "user_id" not in session:
        return False

    if session["role"] != "common":
        return False

    return True


# Voir tout le stock de sa branche
@stock_bp.route("/stock", methods=["GET"])
def get_stock():

    if not check_common_user():
        return jsonify({
            "message": "Forbidden"
        }), 403

    db = SessionLocal()

    stocks = db.query(Stock).filter(
        Stock.branch_id == session["branch_id"]
    ).all()

    result = []

    for stock in stocks:
        result.append({
            "product_id": stock.product_id,
            "quantity": stock.quantity
        })

    db.close()

    return jsonify(result)


# Vérifier la quantité d'un produit précis
@stock_bp.route("/stock/<int:product_id>", methods=["GET"])
def check_stock(product_id):

    if not check_common_user():
        return jsonify({
            "message": "Forbidden"
        }), 403

    db = SessionLocal()

    stock = db.query(Stock).filter(
        Stock.branch_id == session["branch_id"],
        Stock.product_id == product_id
    ).first()

    db.close()

    if stock is None:
        return jsonify({
            "product_id": product_id,
            "quantity": 0
        })

    return jsonify({
        "product_id": product_id,
        "quantity": stock.quantity
    })


# Ajouter du stock
@stock_bp.route("/stock/add", methods=["POST"])
def add_stock():

    if not check_common_user():
        return jsonify({
            "message": "Forbidden"
        }), 403

    data = request.get_json()

    product_id = data.get("product_id")
    quantity = data.get("quantity")

    if not isinstance(quantity, int) or quantity <= 0:
        return jsonify({
            "message": "Quantity must be positive"
        }), 400

    db = SessionLocal()

    stock = db.query(Stock).filter(
        Stock.branch_id == session["branch_id"],
        Stock.product_id == product_id
    ).first()

    if stock:

        stock.quantity += quantity

    else:

        stock = Stock(
            branch_id=session["branch_id"],
            product_id=product_id,
            quantity=quantity
        )

        db.add(stock)

    db.commit()
    db.close()

    return jsonify({
        "message": "Stock added"
    })


# Retirer du stock
@stock_bp.route("/stock/remove", methods=["POST"])
def remove_stock():

    if not check_common_user():
        return jsonify({
            "message": "Forbidden"
        }), 403

    data = request.get_json()

    product_id = data.get("product_id")
    quantity = data.get("quantity")

    if not isinstance(quantity, int) or quantity <= 0:
        return jsonify({
            "message": "Quantity must be positive"
        }), 400

    db = SessionLocal()

    stock = db.query(Stock).filter(
        Stock.branch_id == session["branch_id"],
        Stock.product_id == product_id
    ).first()

    if stock is None:

        db.close()

        return jsonify({
            "message": "Product not found"
        }), 404

    if stock.quantity < quantity:

        db.close()

        return jsonify({
            "message": "Not enough stock"
        }), 400

    stock.quantity -= quantity

    db.commit()
    db.close()

    return jsonify({
        "message": "Stock removed"
    })