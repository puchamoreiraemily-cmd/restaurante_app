from modelos.producto import Producto
from modelos.cliente import Cliente

class SistemaRestaurante:
    """
    Clase que gestiona la lógica de negocio del restaurante Sabor Amazónico.
    """
    def __init__(self):
        self.__menu = {}
        self.__pedidos_actuales = []

    def registrar_producto(self, producto: Producto):
        self.__menu[producto.get_codigo()] = producto
        print(f"✔️ Producto registrado con éxito: {producto.get_nombre()}")

    def mostrar_menu(self):
        print("\n--- MENÚ DE SABOR AMAZÓNICO ---")
        for producto in self.__menu.values():
            print(f"[{producto.get_codigo()}] {producto.get_nombre()} ({producto.get_categoria()}) - ${producto.get_precio():.2f}")
        print("-" * 37)

    def agregar_al_pedido(self, codigo_producto: str):
        if codigo_producto in self.__menu:
            producto = self.__menu[codigo_producto]
            self.__pedidos_actuales.append(producto)
            return True
        return False

    def generar_factura(self, cliente: Cliente):
        if not self.__pedidos_actuales:
            print("No hay consumos registrados para generar una factura.")
            return

        print("\n=====================================")
        print("        FACTURA: Sabor Amazónico     ")
        print("=====================================")
        print(f"{cliente}")
        print(f"Items pedidos: {len(self.__pedidos_actuales)}")
        print("\nDetalle del consumo:")
        
        total = 0.0
        for prod in self.__pedidos_actuales:
            print(f" - {prod.get_nombre():<20} $ {prod.get_precio():.2f}")
            total += prod.get_precio()
            
        print("-" * 37)
        print(f"TOTAL A PAGAR:        $ {total:.2f}")
        print("=====================================\n")
