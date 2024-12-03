# app/models.py
from app import db
from datetime import datetime


class Product(db.Model):
    __tablename__ = "productos"

    id = db.Column(db.Integer, primary_key=True)
    producto = db.Column(db.String(20), nullable=False)
    cantidad = db.Column(db.Float, nullable=False)
    precio_unitario = db.Column(db.Float, nullable=False)
    precio_total = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Product {self.producto}>"


class User(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(50), unique=True, nullable=False)
    contrasena = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<User {self.usuario}>"
