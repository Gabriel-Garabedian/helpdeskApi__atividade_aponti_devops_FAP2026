import json

from flask import Blueprint
from flask import jsonify

usuarios_bp = Blueprint("usuarios", __name__)


@usuarios_bp.get("/usuarios")
def listar():

    with open("data/usuarios.json", encoding="utf-8") as f:

        return jsonify(json.load(f))
