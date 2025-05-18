---
title: "Practica 2"
date: 2025-02-21T10:21:34-08:00
draft: false
---


**Programa Biblioteca.py**

Este programa es un sistema para administrar una biblioteca.
Facilita la gestión de préstamos y devoluciones de libros, la organización del catálogo (añadiendo y mostrando libros), y el manejo de información de los miembros para los préstamos.
Se implementó utilizando el lenguaje de programación Python.

**Nombres:**

* **Funciones:** Incluyen `Book_id`, `title`, `author`, `quantity` y `choice`.
* **Variables:** Se utilizan `Book`, `DigitalBook`, `Library`, `Member` y `Genre`.
* **Estructuras:** Se definen `add_book`, `display_books`, `from_dict` y `main`.

**Objetos:**

El programa trabaja con objetos como `Book`, `DigitalBook`, `Member` y `Library`.
`Book` y `DigitalBook` representan los libros físicos y digitales, `Member` modela a los usuarios de la biblioteca, y `Library` contiene el catálogo de libros y la información de los miembros.

**Entornos:**

El programa opera en un entorno que combina el uso de archivos para el almacenamiento de datos y la gestión dinámica de la memoria, con `memory_management` para la liberación de recursos.
También se emplean listas para organizar tanto los objetos (libros) como los datos.

**Bloques:**

El código está estructurado en bloques que utilizan construcciones de control como bucles (`while`, `for`) y condicionales (`if`, `else`, `elif`).

**Alcance:**

* **Local:** Las variables declaradas dentro de las funciones (por ejemplo, `book_id`, `title`, `choice`, `book`, `data`) tienen alcance local.
* **Estático:** La clase `Genre` define miembros estáticos como `FICTION`, `NON_FICTION`, `SCIENCE`, `HISTORY`, `FANTASY`, `BIOGRAPHY` y `OTHER`.
* **Global:** No se utilizan variables con alcance global en este programa.

**Administración de memoria:**

El programa utiliza `memory_management.increment_heap_allocations()` y `memory_management.increment_heap_deallocations()` para llevar un registro de la asignación y liberación de memoria en el heap, respectivamente.
Estas funciones se invocan exclusivamente en los métodos `__init__` y `__def__`.

**Expresiones:**

El código incluye conversiones de tipo (como `int(input(...))`), operaciones aritméticas (por ejemplo, `book.quantity -= 1`) y expresiones condicionales (usando `if` y `else`, como en `book if book else None`).

**Comandos:**

Se utilizan comandos para la entrada y salida de datos (`print`, `int(input(...))`), así como para el manejo de archivos (`with open(...)` y `except` para el manejo de errores).

**Secuencia:**

El programa se organiza definiendo primero las clases, que luego se instancian según sea necesario.
El flujo de ejecución principal comienza en la función `main()`, que carga los datos iniciales de libros y miembros desde archivos y luego presenta un menú al usuario.
Las acciones se ejecutan en respuesta a las opciones seleccionadas por el usuario.

**Selección:**

Las estructuras condicionales (`if`, `elif`, `else`) se utilizan para implementar la toma de decisiones, por ejemplo, para verificar si un libro o un miembro ya está registrado antes de realizar una operación.

**Iteración:**

Se utiliza un bucle `while` para mostrar el menú principal de la biblioteca y permitir al usuario elegir repetidamente una acción.
Los bucles `for` se emplean, por ejemplo, para buscar libros y notificar al usuario si un libro está disponible.

**Recursión:**

Este programa no emplea técnicas de recursión.

**Subprogramas:**

El programa se estructura mediante la definición de varias funciones, algunas de las cuales están diseñadas para ser reutilizadas en diferentes partes del código.

**Tipos de datos:**

* **Primitivos:** Se utilizan tipos de datos básicos como `int`, `str` y `bool`.
* **Compuestos:** El programa también emplea estructuras de datos más complejas, como `list` y `dict`.

**Herencia:**

La clase `DigitalBook` hereda de la clase `Book`, lo que permite a `DigitalBook` utilizar los métodos ya definidos en `Book`.

**Encapsulamiento:**

El programa implementa encapsulamiento, aunque de forma parcial.
Esto significa que algunos atributos (como `id` y `title`) se definen dentro de los objetos y se manipulan mediante métodos, pero no están completamente protegidos contra el acceso externo.

**Polimorfismo:**

El polimorfismo se manifiesta, por ejemplo, en el método `Book.to_dict()`, que se redefine en la clase `DigitalBook` para adaptarlo a las necesidades específicas de esta clase.

**Subtipos:**

La relación de subtipo se observa en `DigitalBook`, que es un subtipo de `Book` y, por lo tanto, hereda sus características.

---

**Memory\_management.py**

Este programa se dedica a la gestión de la memoria durante la ejecución del programa principal, asignando y liberando memoria según sea necesario.
Está desarrollado en Python.

**Nombres:**

* **Funciones:** Incluye `__init__`, `increment_heap_allocations`, `increment_heap_deallocations` y `display_memory_usage`.
* **Variables:** Se utilizan `heap_allocations`, `heap_deallocations`, `memory_management` y `size`.
* **Estructuras:** La principal estructura es la clase `MemoryManagement`.

**Objetos:**

Los objetos clave en este programa son la clase `MemoryManagement` en sí, que define cómo se gestiona la memoria, y `memory_management`, que es una instancia de esta clase.

**Entornos:**

Todo el código del programa se encuentra dentro de la definición de la clase `MemoryManagement`.

**Bloques:**

El programa se organiza en bloques que corresponden a la definición de la clase `MemoryManagement` y a la definición de las funciones que contiene (como `__init__`).

**Alcance:**

* **Global:** La variable `memory_management` tiene alcance global.
* **Local:** Las variables `heap_allocations`, `heap_deallocations` y `size` son locales a las funciones en las que se declaran.

**Administración de memoria:**

La función principal de este programa es llevar la cuenta de las asignaciones y liberaciones de memoria que ocurren en el heap.

**Expresiones:**

El programa utiliza expresiones matemáticas para incrementar los contadores `heap_allocations` y `heap_deallocations`.

**Comandos:**

El programa utiliza principalmente comandos de salida, específicamente la función `print`.

**Secuencia:**

La secuencia de ejecución implica primero definir la clase `MemoryManagement`, luego definir sus métodos (las funciones dentro de la clase) y finalmente crear un objeto (una instancia) de esa clase.

**Selección:**

Este programa no utiliza estructuras de control condicionales.

**Iteración:**

El programa no contiene bucles de ningún tipo.

**Recursión:**

No se emplea recursión en este programa.

**Subprogramas:**

Los métodos definidos dentro de la clase `MemoryManagement` actúan como subprogramas.

**Tipos de datos:**

* **Primitivos:** Se utilizan tipos de datos básicos como `int` y `str`.
* **Compuestos:** También se utiliza el tipo `object`.

**Herencia:**

En este programa, no hay herencia; no se hereda de ninguna clase existente, ni otras clases heredan de `MemoryManagement`.

**Encapsulamiento:**

El programa gestiona atributos relacionados con la memoria (como `heap_allocations` y `heap_deallocations`) mediante métodos, lo que representa una forma de encapsulamiento.
Sin embargo, estos atributos no están completamente protegidos.

**Polimorfismo:**

Este programa no hace uso del polimorfismo.

**Subtipos:**

No hay relaciones de subtipo presentes en este programa.

---

**Biblioteca\_web.py**

Este archivo contiene el código para la aplicación web del programa principal, `biblioteca.py`.
Utiliza el framework Flask para construir una API REST que soporta operaciones CRUD (Crear, Leer, Actualizar y Borrar) sobre los libros y los miembros de la biblioteca.

**Nombres:**

* **Funciones:** Incluye `index`, `get_books`, `get_members`, `add_book`, `add_member`, `issue_book`, `return_book`, `save`, `load` y `get_genres`.
* **Variables:** Se utilizan `app`, `library`, `data`, `books`, `members`, `book`, `member`, `book_id`, `member_id`, `is_digital` y `genres`.
* **Estructuras:** Se emplean Flask, y las clases `Book`, `DigitalBook`, `Member`, `Library` y `Genre`.

**Objetos:**

El programa trabaja con instancias de varias clases, incluyendo `library`, `book`, `member` y `memory_management`.

**Entornos:**

Este programa está diseñado para ejecutarse en un entorno de servidor web local, permitiendo a los usuarios interactuar con la biblioteca a través de la web.

**Bloques:**

El código se organiza en bloques que utilizan estructuras condicionales (`if`, `else`) y bucles (`for`).

**Alcance:**

* **Global:** Las variables `app`, `library` y `memory_management` tienen alcance global.
* **Local:** Las variables como `data` y `book_id` son locales a las funciones donde se definen.

**Administración de memoria:**

El programa utiliza `memory_management` para gestionar la liberación de memoria durante su ejecución.

**Expresiones:**

El código incluye asignaciones de funciones (como `data = request.json`), condicionales (`if is_digital`), llamadas a funciones que retornan valores (como `jsonify(book.to_dict())`) y operaciones con operadores (como `book_id = int(data['book_id'])`).

**Comandos:**

* **Entrada:** Se utiliza `request.json` para recibir datos en solicitudes HTTP.
* **Salida:** Se emplea `print()` para mostrar información.
* **Archivos:** Se llama a `load_library_from_file()` para cargar datos desde un archivo y a `sabe_library_to_file()` para guardar datos en un archivo.

**Secuencia:**

El programa sigue una secuencia que comienza con la carga de las librerías necesarias, seguida de la inicialización de la aplicación Flask, la creación de una instancia de la biblioteca, la carga de datos de libros y miembros desde archivos y finalmente, la ejecución del servidor Flask.

**Selección:**

Se utilizan condicionales `if` y `else` para decidir si se debe crear un libro digital o físico y para asegurar que el archivo se está ejecutando como el programa principal del servidor.

**Iteración:**

Se emplea un bucle `for` para convertir listas de libros y miembros a formato JSON.

**Recursión:**

Este programa no utiliza recursión.

**Subprogramas:**

El programa se estructura en subprogramas, incluyendo funciones definidas con `def` (como `index`, `get_books`, etc.) y funciones importadas (como `memory_management.display_memory_usage`).

**Tipos de datos:**

* **Primitivos:** Se utilizan tipos básicos como `int`, `str`, `bool` y `None`.
* **Compuestos:** Se emplean `dict`, `list` y `object`.

**Herencia:**

Al igual que en el programa principal, la clase `DigitalBook` hereda de la clase `Book`.

**Encapsulamiento:**

El programa utiliza objetos como `library` y `member`, que encapsulan datos y los manipulan a través de métodos.

**Polimorfismo:**

El polimorfismo se ejemplifica en la función `library.add_book()`, que puede aceptar objetos tanto de la clase `DigitalBook` como de la clase `Book`.

**Subtipos:**

`DigitalBook` es un subtipo de `Book`, lo que permite que los objetos de la primera clase se utilicen en contextos donde se espera un objeto de la segunda.

---

**Conclusiones**

El análisis detallado del programa principal de la biblioteca, el módulo de gestión de memoria y la aplicación web ha permitido desglosar su estructura y las características de cada componente.
Cada programa cumple una función específica dentro del sistema general.
Este análisis facilita la comprensión del código, la identificación y corrección de errores, el mantenimiento de una estructura coherente, la optimización del rendimiento y el control sobre las distintas funcionalidades.

**Repositorio:**

[https://github.com/demoncybor/Practica2](https://github.com/demoncybor/Practica2)
