class Prenda:
    def __init__(self, ID, nombre, talle, precio, material, color):
        self.ID = ID
        self.nombre = nombre
        self.talle = talle
        self.precio = precio
        self.material = material
        self.color = color
        self.__secretPassword = "1234"

    def serialize(self):
        return {
            'ID': self.ID,
            'nombre': self.nombre,
            'precio': self.precio,
            'talle': self.talle
        }

    def serialize_details(self):
        return {
            'ID': self.ID,
            'nombre': self.nombre,
            'talle': self.talle,
            'precio': self.precio,
            'material': self.material,
            'color': self.color,
        }


class PrendaConDescuento(Prenda):
    def __init__(self, ID, nombre, talle, precio, material, color, descuento=0):
        super().__init__(ID, nombre, talle, precio, material, color)
        self.descuento = descuento

    def serialize_details(self):
        details = super().serialize_details()
        self.precio = self.precio * (1 - (self.descuento / 100))
        details['descuento'] = self.descuento
        details['precio'] = self.precio
        return details
