# app/utils.py
from marshmallow import Schema, fields, validate


class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    producto = fields.Str(required=True, validate=validate.Length(min=1, max=20))
    cantidad = fields.Float(required=True, validate=validate.Range(min=0))
    precio_unitario = fields.Float(required=True, validate=validate.Range(min=0))
    precio_total = fields.Float(dump_only=True)
    created_at = fields.DateTime(dump_only=True)


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    usuario = fields.Str(required=True, validate=validate.Length(min=3, max=50))
    contrasena = fields.Str(
        required=True, validate=validate.Length(min=4, max=50), load_only=True
    )
    created_at = fields.DateTime(dump_only=True)
