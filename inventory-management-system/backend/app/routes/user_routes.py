from flask import Blueprint, request, jsonify, session

from app.database import SessionLocal
from app.models.user import User
from app.auth.authentication import hash_password


user_bp = Blueprint("users", __name__)


# Liste des utilisateurs (admin uniquement)
@user_bp.route("/users", methods=["GET"])
def list_users():

    if "user_id" not in session:
        return jsonify({"message": "Unauthorized"}), 401

    if session["role"] != "admin":
        return jsonify({"message": "Forbidden"}), 403

    db = SessionLocal()

    users = db.query(User).all()

    result = []

    for user in users:
        result.append({
            "id": user.id,
            "username": user.username,
            "role": user.role,
            "branch_id": user.branch_id,
            "deleted": user.is_deleted
        })

    db.close()

    return jsonify(result)


# Création d'un utilisateur commun (admin uniquement)
@user_bp.route("/users/create", methods=["POST"])
def create_user():

    if "user_id" not in session:
        return jsonify({"message": "Unauthorized"}), 401

    if session["role"] != "admin":
        return jsonify({"message": "Forbidden"}), 403

    data = request.get_json()

    db = SessionLocal()

    user = User(
        username=data["username"],
        password_hash=hash_password(data["password"]),
        role="common",
        branch_id=data["branch_id"]
    )

    db.add(user)
    db.commit()
    db.close()

    return jsonify({
        "message": "User created"
    })


# Suppression logique (soft delete)
@user_bp.route("/users/delete/<int:user_id>", methods=["PUT"])
def delete_user(user_id):

    if "user_id" not in session:
        return jsonify({"message": "Unauthorized"}), 401

    if session["role"] != "admin":
        return jsonify({"message": "Forbidden"}), 403

    db = SessionLocal()

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if user is None:
        db.close()
        return jsonify({
            "message": "User not found"
        }), 404

    user.is_deleted = True

    db.commit()
    db.close()

    return jsonify({
        "message": "User deleted"
    })


# Changer le mot de passe d'un utilisateur (admin uniquement)
@user_bp.route("/users/password/<int:user_id>", methods=["PUT"])
def change_password(user_id):

    if "user_id" not in session:
        return jsonify({"message": "Unauthorized"}), 401

    if session["role"] != "admin":
        return jsonify({"message": "Forbidden"}), 403

    data = request.get_json()

    db = SessionLocal()

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if user is None:
        db.close()
        return jsonify({
            "message": "User not found"
        }), 404

    user.password_hash = hash_password(
        data["password"]
    )

    db.commit()
    db.close()

    return jsonify({
        "message": "Password updated"
    })


# Changer la branche d'un utilisateur (admin uniquement)
@user_bp.route("/users/branch/<int:user_id>", methods=["PUT"])
def change_branch(user_id):

    if "user_id" not in session:
        return jsonify({"message": "Unauthorized"}), 401

    if session["role"] != "admin":
        return jsonify({"message": "Forbidden"}), 403

    data = request.get_json()

    db = SessionLocal()

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if user is None:
        db.close()
        return jsonify({
            "message": "User not found"
        }), 404

    user.branch_id = data["branch_id"]

    db.commit()
    db.close()

    return jsonify({
        "message": "Branch updated"
    })