import csv
from clase_prenda import Prenda


def cargar_prendas():
    prendas = []
    with open("prendas.csv", "r") as prendas_file:
        rows = csv.DictReader(prendas_file)

        for row in rows:
            prendas.append(
                Prenda(
                    row["ID"],
                    row["nombre"],
                    row["talle"],
                    row["precio"],
                    row["material"],
                    row["color"],
                    row["descuento"]
                )
            )
        return prendas


headers = ["ID", "nombre", "talle", "precio", "material", "color", "descuento"]


def create_prendas(prenda_add):
    with open("prendas.csv", "a") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=headers)
        if output_file.tell() == 0:
            writer.writeheader()
        writer.writerow(prenda_add)


def modificar_prendas(prenda_modify):
    with open("prendas.csv", "r") as input_file:
        rows = list(csv.DictReader(input_file))

    for row in rows:
        if (int(row["ID"]) == prenda_modify["ID"]):
            for key in prenda_modify:
                row[key] = prenda_modify[key]

    with open("prendas.csv", "w", newline='') as output_file:
        writer = csv.DictWriter(output_file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)


def prenda_descuento(ID, descuento):
    with open("prendas.csv", "r") as input_file:
        rows = list(csv.DictReader(input_file))
        for row in rows:
            if row["ID"] == ID:
                prenda_modify = row
                prenda_modify["descuento"] = descuento
                modificar_prendas(prenda_modify)


def borrar_prendas(ID):
    contenido = []
    with open("prendas.csv", "r") as input_file:
        rows = list(csv.DictReader(input_file))
        for row in rows:
            if row["ID"] != ID:
                contenido.append(row)
    with open("prendas.csv", "w") as output_file:
        for row in contenido:
            create_prendas(row)