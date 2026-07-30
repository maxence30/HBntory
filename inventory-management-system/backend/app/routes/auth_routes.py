from flask import Blueprint, request, session, jsonify

from app.database import SessionLocal
from app.auth.authentication import authenticate_user


auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    db = SessionLocal()

    user = authenticate_user(
        db,
        username,
        password
    )

    db.close()

    if user is None:
        return jsonify({
            "message": "Invalid credentials"
        }), 401

    session["user_id"] = user.id
    session["role"] = user.role
    session["branch_id"] = user.branch_id

    return jsonify({
        "message": "Login successful",
        "username": user.username,
        "role": user.role
    })


@auth_bp.route("/profile", methods=["GET"])
def profile():

    if "user_id" not in session:
        return jsonify({
            "message": "Unauthorized"
        }), 401

    return jsonify({
        "user_id": session["user_id"],
        "role": session["role"],
        "branch_id": session["branch_id"]
    })


@auth_bp.route("/logout", methods=["POST"])
def logout():

    session.clear()

    return jsonify({
        "message": "Logged out"
    })