#  Desarrollo de un Sistema Modular de Gestión para el Restaurante "Sabor Amazónico"

**Estudiante:** Emily Silvana Pucha Moreira  
**Institución:** Universidad Estatal Amazónica  
**Carrera:** Tecnologías de la Información  
**Asignatura:** Programación Orientada a Objetos (POO)  
**Semana:** Semana 4 - Arquitectura Avanzada y Modularización de Software  

---

##  1. Introducción y Propósito del Proyecto

El desarrollo de software moderno exige mucho más que simplemente escribir código que funcione; requiere orden, estructura y una separación clara de las responsabilidades de cada componente. Este proyecto nace bajo esa premisa, simulando el funcionamiento real de la gestión de comandas y facturación de un restaurante enfocado en la gastronomía local, denominado **Sabor Amazónico**.

El objetivo principal de esta aplicación es plasmar de forma práctica los pilares de la **Programación Orientada a Objetos (POO)** en Python 3, resolviendo un problema común en los sistemas de información: cómo estructurar un programa para que pueda crecer en el futuro sin volverse caótico. A través de la modularización, el sistema procesa de forma independiente la información de los clientes, la administración del menú disponible y el cálculo aritmético complejo para la emisión de comprobantes o facturas finales.

---

##  2. Objetivos Académicos y Técnicos

1. **Aplicar el Encapsulamiento Riguroso:** Proteger la integridad de los datos sensibles (como la cédula o los precios) impidiendo el acceso directo a los atributos desde fuera de las clases, utilizando en su lugar métodos de acceso públicos (`getters`).
2. **Implementar Separación de Responsabilidades (SoC):** Dividir el programa en carpetas lógicas (`modelos` y `servicios`) para garantizar que las reglas del negocio no se mezclen con las estructuras de datos puras.
3. **Gestionar Colecciones Dinámicas:** Utilizar diccionarios y listas mutables para administrar el menú del restaurante y las comandas de los clientes en tiempo real dentro de la memoria del sistema.

---

##  3. Arquitectura del Software y Estructura del Directorio

Para evitar el acoplamiento difuso (donde un cambio en un archivo rompe todo el programa), se diseñó una estructura de directorios limpia y profesional. Las dependencias fluyen de manera unidireccional, lo que facilita enormemente el mantenimiento del código:

```text
restaurante_app/
│
├── modelos/
│   ├── __init__.py      # Inicializador del paquete de modelos
│   ├── cliente.py       # Estructura y encapsulamiento del Cliente
│   └── producto.py      # Estructura y comportamiento del Producto
│
├── servicios/
│   ├── __init__.py      # Inicializador del paquete de servicios
│   └── restaurante.py   # Lógica central del negocio y facturación
│
└── main.py              # Punto de entrada y ejecución del sistema
