class Producto:
    """
    Clase que representa un producto del menú del restaurante.
    """
    def __init__(self, codigo: str, nombre: str, precio: float, categoria: str):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio
        self.__categoria = categoria

    # Métodos Getter
    def get_codigo(self) -> str:
        return self.__codigo

    def get_nombre(self) -> str:
        return self.__nombre

    def get_precio(self) -> float:
        return self.__precio

    def get_categoria(self) -> str:
        return self.__categoria

    def __str__(self) -> str:
        return f"[{self.__codigo}] {self.__nombre} ({self.__categoria}) - ${self.__precio:.2f}"
