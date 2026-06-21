from modelos.cliente import Cliente
from modelos.producto import Producto
from servicios.restaurante import SistemaRestaurante

def main():
    print("=== Iniciando Sistema de Gestión de Restaurante ===\n")
    sistema = SistemaRestaurante()

    # 1. Registro inicial del Menú
    print("--- Registrando Productos en el Menú ---")
    sistema.registrar_producto(Producto("101", "Maito de Pescado", 8.50, "Plato Fuerte"))
    sistema.registrar_producto(Producto("102", "Pizza de Mayón", 12.00, "Plato Fuerte"))
    sistema.registrar_producto(Producto("201", "Chicha de Chonta", 1.50, "Bebida"))
    sistema.registrar_producto(Producto("301", "Ceviche de Hongos", 4.50, "Entrada"))

    # 2. Despliegue del Menú
    sistema.mostrar_menu()

    # 3. Simulación de una comanda para el Cliente
    cliente_estudiante = Cliente("Emily Pucha", "2200112233")
    
    # Agregar consumos
    sistema.agregar_al_pedido("102")  # Pizza de Mayón
    sistema.agregar_al_pedido("201")  # Chicha de Chonta

    # 4. Generación de factura final
    sistema.generar_factura(cliente_estudiante)

if __name__ == "__main__":
    main()
