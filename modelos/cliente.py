class Cliente:
    def __init__(self, nombre: str, cedula: str):
        self.__nombre = nombre
        self.__cedula = cedula

    def get_nombre(self) -> str:
        return self.__nombre

    def get_cedula(self) -> str:
        return self.__cedula

    def __str__(self) -> str:
        return f"Cliente: {self.__nombre} (C.I.: {self.__cedula})"
