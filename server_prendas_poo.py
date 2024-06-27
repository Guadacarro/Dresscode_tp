from flask import Flask, jsonify, request
import prendas_controller_poo
from db_prendas import create_tables
from exchange_rate import get_xr
import db_manager

app = Flask(__name__)


@app.route('/prendas', methods=["GET"])
def get_prendas():
    prendas = prendas_controller_poo.get_prenda()
    prendas_list = []
    for prenda in prendas:
        elem = prenda.serialize_details()
        prendas_list.append(elem)
    return jsonify(prendas_list)


@app.route("/prenda/crear", methods=["POST"])
def insert_prenda():
    prenda_details = request.get_json()
    ID = prenda_details["ID"]
    nombre = prenda_details["nombre"]
    talle = prenda_details["talle"]
    precio = prenda_details["precio"]
    material = prenda_details["material"]
    color = prenda_details["color"]
    result = prendas_controller_poo.insert_prenda(ID, nombre, talle, precio, material, color)
    db_manager.create_prendas(prenda_details)
    return jsonify(result)


quince_prendas = [
    {
        "ID": 1,
        "nombre": "camisa",
        "talle": 16,
        "precio": 25000,
        "material": "algodón",
        "color": "azul"
    },
    {
        "ID": 2,
        "nombre": "falda",
        "talle": 10,
        "precio": 18000,
        "material": "poliéster",
        "color": "negra"
    },
    {
        "ID": 3,
        "nombre": "pantalon",
        "talle": 16,
        "precio": 32000,
        "material": "seda",
        "color": "roja"
    },
    {
        "ID": 4,
        "nombre": "chaqueta",
        "talle": 50,
        "precio": 45000,
        "material": "cuero",
        "color": "marrón"
    },
    {
        "ID": 5,
        "nombre": "blusa",
        "talle": 20,
        "precio": 21000,
        "material": "seda",
        "color": "blanca"
    },
    {
        "ID": 6,
        "nombre": "jeans",
        "talle": 32,
        "precio": 29000,
        "material": "mezclilla",
        "color": "azul claro"
    },
    {
        "ID": 7,
        "nombre": "vestido",
        "talle": 20,
        "precio": 37000,
        "material": "seda",
        "color": "verde"
    },
    {
        "ID": 8,
        "nombre": "shorts",
        "talle": 16,
        "precio": 22000,
        "material": "algodón",
        "color": "amarillo"
    },
    {
        "ID": 9,
        "nombre": "sudadera",
        "talle": 23,
        "precio": 26000,
        "material": "poliéster",
        "color": "gris"
    },
    {
        "ID": 10,
        "nombre": "polo",
        "talle": 5,
        "precio": 20000,
        "material": "algodón",
        "color": "rojo"
    },
    {
        "ID": 11,
        "nombre": "buzo",
        "talle": 9,
        "precio": 30000,
        "material": "algodón",
        "color": "verde oliva"
    },
    {
        "ID": 12,
        "nombre": "chomba",
        "talle": 16,
        "precio": 27000,
        "material": "lana",
        "color": "azul marino"
    },
    {
        "ID": 13,
        "nombre": "leggins",
        "talle": 16,
        "precio": 24000,
        "material": "spandex",
        "color": "negro"
    },
    {
        "ID": 14,
        "nombre": "abrigo",
        "talle": 16,
        "precio": 50000,
        "material": "lana",
        "color": "gris oscuro"
    },
    {
        "ID": 15,
        "nombre": "calcetines",
        "talle": 5,
        "precio": 8000,
        "material": "algodón",
        "color": "blanco"
    }
]


@app.route("/prenda/crear/15", methods=["POST"])
def insert_prenda_quince():
    for prenda_details in quince_prendas:
        ID = prenda_details["ID"]
        nombre = prenda_details["nombre"]
        talle = prenda_details["talle"]
        precio = prenda_details["precio"]
        material = prenda_details["material"]
        color = prenda_details["color"]
        prendas_controller_poo.insert_prenda(ID, nombre, talle, precio, material, color)
        db_manager.create_prendas(prenda_details)
    return "status ok"


# funcion para escribir 15 de una en la db (solo para produccion)


@app.route("/prenda/modificar", methods=["PUT"])
def update_prenda():
    prenda_details = request.get_json()
    ID = prenda_details["ID"]
    nombre = prenda_details["nombre"]
    talle = prenda_details["talle"]
    precio = prenda_details["precio"]
    material = prenda_details["material"]
    color = prenda_details["color"]

    db_manager.modificar_prendas(prenda_details)

    result = prendas_controller_poo.update_prenda(ID, nombre, talle, precio, material, color)
    return jsonify(result)


@app.route("/prenda/eliminar/<ID>", methods=["DELETE"])
def delete_prenda(ID):
    db_manager.borrar_prendas(ID)
    result = prendas_controller_poo.delete_prenda(ID)
    return jsonify(result)


@app.route("/prenda/<ID>", methods=["GET"])
def get_prenda_by_id(ID):
    prenda = prendas_controller_poo.get_by_id(ID)
    return jsonify(prenda)


@app.route("/prenda/descuento/<ID>", methods=["PUT"])
def prenda_descuento(ID):
    req = request.get_json()
    descuento = req["descuento"]

    res = prendas_controller_poo.prenda_descuento(ID, descuento)
    db_manager.prenda_descuento(ID, descuento)
    return jsonify(res)


@app.route("/prenda/oferta", methods=["GET"])
# Es para implementar polimorfismo, es mas facil llamar a la DB
# con el statement WHERE descuento IS NOT NULL
def prenda_oferta():
    res = prendas_controller_poo.prenda_oferta()
    return jsonify(res)


@app.route("/prenda/usd/<ID>", methods=["GET"])
def get_prenda_by_id_usd(ID):
    prenda = prendas_controller_poo.get_by_id(ID)
    xr = get_xr()
    print(prenda)
    price_usd = prenda['precio'] / xr
    prenda['precio'] = round(price_usd, 2)
    return jsonify(prenda)


create_tables()

if __name__ == '__main__':
    app.run(debug=True)