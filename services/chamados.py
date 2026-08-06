import json

from flask import Blueprint
from flask import jsonify
from flask import request

ARQUIVO="data/chamados.json"

chamados_bp=Blueprint("chamados",__name__)

def ler():

    with open(ARQUIVO,encoding="utf-8") as f:
        return json.load(f)

def salvar(dados):

    with open(ARQUIVO,"w",encoding="utf-8") as f:
        json.dump(dados,f,indent=4,ensure_ascii=False)

@chamados_bp.get("/chamados")
def listar():

    return jsonify(ler())

@chamados_bp.post("/chamados")
def adicionar():

    chamados=ler()

    novo=request.json

    novo["id"]=len(chamados)+1

    chamados.append(novo)

    salvar(chamados)

    return novo,201