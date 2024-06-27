from flask import request, jsonify
from db_prendas import get_db
from clase_prenda  import Prenda, PrendaConDescuento

def prenda_descuento(ID, descuento):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE prendas SET descuento = ? WHERE ID = ?"
    cursor.execute(statement, [descuento, ID])
    db.commit()
    return True

def insert_prenda(ID, nombre, talle, precio, material, color):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO prendas (ID, nombre, talle, precio, material, color) \
    VALUES ( ?, ?, ?, ? ,?, ?)"
    cursor.execute(statement, [ID, nombre, talle, precio, material, color])
    db.commit()
    return True

def update_prenda(ID, nombre, talle, precio, material, color):
    db = get_db()
    cursor = db.cursor()
    statement = """
        UPDATE prendas 
        SET nombre = ?, talle = ?, precio = ?, material = ?, color = ? \
        WHERE ID = ?
    """
    cursor.execute(statement, [nombre, talle, precio, material, color, ID])
    db.commit()
    return True

def delete_prenda(ID):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM prendas WHERE ID = ?"
    cursor.execute(statement, [ID])
    db.commit()
    return True

def prenda_oferta():
    list_prenda = get_prenda()
    list_res = []
    for prenda in list_prenda:
        if (isinstance(prenda, PrendaConDescuento)):
            list_res.append(prenda.serialize_details())
    return list_res

def get_by_id(ID):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT ID, nombre, talle, precio, material, color, descuento FROM prendas WHERE ID = ?"
    cursor.execute(statement, [ID])
    single_prenda = cursor.fetchone()
    ID = single_prenda[0]
    nombre = single_prenda[1]
    talle = single_prenda[2]
    precio = single_prenda[3]
    material = single_prenda[4]
    color = single_prenda[5]
    if (single_prenda[6]):
            descuento = single_prenda[6]
            prenda = PrendaConDescuento(ID, nombre, talle, precio, material, color, descuento)
    else:
        prenda = Prenda(ID, nombre, talle, precio, material, color)
    return prenda.serialize_details()


def get_prenda():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM prendas"
    cursor.execute(query)
    prenda_list = cursor.fetchall()
    list_of_prendas=[]
    for prenda in prenda_list:
        ID = prenda[0]
        nombre = prenda[1]
        talle = prenda[2]
        precio = prenda[3]
        material = prenda[4]
        color = prenda[5]
        if (prenda[6]):
            descuento = prenda[6]
            prenda_to_add = PrendaConDescuento(ID, nombre, talle, precio, material, color, descuento)
            # Nota: en la base de datos, el descuento no se va a aplicar
            # solo se va a aplicar el descuento en el get_prendas, asi si quiero cambiar el descuento
            # guardo el valor original, y es mas dinamico para ir cambiando descuentos
        else:
            prenda_to_add = Prenda(ID, nombre, talle, precio, material, color)

        list_of_prendas.append(prenda_to_add)
    return list_of_prendas