from flask import Blueprint, request, jsonify
from app.services import ProductService, UserService
from marshmallow import ValidationError

product_bp = Blueprint("product", __name__)


# Product Routes
@product_bp.route("/products", methods=["GET"])
def get_products():
    try:
        products = ProductService.get_all_products()
        return jsonify(products), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@product_bp.route("/products", methods=["POST"])
def create_product():
    try:
        data = request.get_json()
        new_product = ProductService.create_product(data)
        return jsonify(new_product), 201
    except ValidationError as ve:
        return jsonify({"error": ve.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@product_bp.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    try:
        product = ProductService.get_product_by_id(product_id)
        return jsonify(product), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404


@product_bp.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    try:
        data = request.get_json()
        updated_product = ProductService.update_product(product_id, data)
        return jsonify(updated_product), 200
    except ValidationError as ve:
        return jsonify({"error": ve.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@product_bp.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    try:
        ProductService.delete_product(product_id)
        return jsonify({"message": "Product deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# User Authentication Routes
@product_bp.route("/register", methods=["POST"])
def register_user():
    try:
        data = request.get_json()
        new_user = UserService.create_user(data)
        return jsonify(new_user), 201
    except ValidationError as ve:
        return jsonify({"error": ve.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@product_bp.route("/login", methods=["POST"])
def login_user():
    try:
        data = request.get_json()
        username = data.get("usuario")
        password = data.get("contrasena")

        if not username or not password:
            return jsonify({"error": "Username and password are required"}), 400

        if UserService.authenticate_user(username, password):
            return jsonify({"message": "Login successful"}), 200
        else:
            return jsonify({"error": "Invalid credentials"}), 401
    except Exception as e:
        return jsonify({"error": str(e)}), 500
