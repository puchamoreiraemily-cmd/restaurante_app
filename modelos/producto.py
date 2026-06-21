# modelos/producto.py

class Producto:
    """Clase que representa un producto (plato o bebida) del restaurante."""
    
    # El constructor inicializa las propiedades de cada producto
    def __init__(self, id_producto: int, nombre: str, precio: float, categoria: str):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria  # Ejemplo: "Plato Fuerte", "Bebida", "Postre"

    # El método especial __str__ define cómo se verá el objeto al usar un print()
    def __str__(self):
        return f"[{self.id_producto}] {self.nombre} ({self.categoria}) - ${self.precio:.2f}"
    
