# app/services.py
from app import db
from app.models import Product, User
from app.utils import ProductSchema, UserSchema
from sqlalchemy.exc import SQLAlchemyError


class ProductService:
    @staticmethod
    def get_all_products():
        try:
            products = Product.query.all()
            return ProductSchema(many=True).dump(products)
        except SQLAlchemyError as e:
            raise Exception(f"Error retrieving products: {str(e)}")

    @staticmethod
    def create_product(data):
        try:
            # Calculate precio_total
            cantidad = data.get("cantidad")
            precio_unitario = data.get("precio_unitario")
            descuento = data.get("descuento", 0)
            precio_total = cantidad * precio_unitario * (1 - descuento / 100)

            # Validate and create product
            product_schema = ProductSchema()
            validated_data = product_schema.load(data)

            new_product = Product(
                producto=validated_data["producto"],
                cantidad=validated_data["cantidad"],
                precio_unitario=validated_data["precio_unitario"],
                precio_total=precio_total,
            )

            db.session.add(new_product)
            db.session.commit()

            return product_schema.dump(new_product)
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Error creating product: {str(e)}")

    @staticmethod
    def get_product_by_id(product_id):
        try:
            product = Product.query.get_or_404(product_id)
            return ProductSchema().dump(product)
        except SQLAlchemyError as e:
            raise Exception(f"Error retrieving product: {str(e)}")

    @staticmethod
    def update_product(product_id, data):
        try:
            product = Product.query.get_or_404(product_id)

            # Validate incoming data
            product_schema = ProductSchema(partial=True)
            validated_data = product_schema.load(data)

            # Update fields
            for key, value in validated_data.items():
                setattr(product, key, value)

            # Recalculate precio_total if needed
            if "cantidad" in validated_data or "precio_unitario" in validated_data:
                cantidad = validated_data.get("cantidad", product.cantidad)
                precio_unitario = validated_data.get(
                    "precio_unitario", product.precio_unitario
                )
                descuento = validated_data.get("descuento", 0)
                product.precio_total = (
                    cantidad * precio_unitario * (1 - descuento / 100)
                )

            db.session.commit()
            return product_schema.dump(product)
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Error updating product: {str(e)}")

    @staticmethod
    def delete_product(product_id):
        try:
            product = Product.query.get_or_404(product_id)
            db.session.delete(product)
            db.session.commit()
            return True
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Error deleting product: {str(e)}")


class UserService:
    @staticmethod
    def create_user(data):
        try:
            user_schema = UserSchema()
            validated_data = user_schema.load(data)

            new_user = User(
                usuario=validated_data["usuario"],
                contrasena=validated_data["contrasena"],
            )

            db.session.add(new_user)
            db.session.commit()

            return user_schema.dump(new_user)
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Error creating user: {str(e)}")

    @staticmethod
    def authenticate_user(username, password):
        try:
            user = User.query.filter_by(usuario=username, contrasena=password).first()
            return user is not None
        except SQLAlchemyError as e:
            raise Exception(f"Error authenticating user: {str(e)}")
