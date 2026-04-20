# Colección de Ejercicios y Pruebas en Python

Este repositorio contiene una colección de 18 ejercicios prácticos en Python, diseñados para mejorar las habilidades de programación y algoritmia. Se han estructurado en carpetas por nivel de dificultad para una mejor organización.

El archivo `resultados_totales.py` en la raíz contiene las soluciones oficiales de todos los ejercicios.

## Estructura del Repositorio

- 📁 **Basico/**: Ejercicios enfocados en entrada/salida de datos, variables y condicionales simples. (Ejercicios 1 a 5, 16, 17 y 18)
- 📁 **Intermedio/**: Ejercicios que introducen bucles anidados, condiciones múltiples y manipulación intermedia de strings. (Ejercicios 6 a 10)
- 📁 **Avanzado/**: Retos algorítmicos complejos como ordenamiento, lógica de juegos y procesamiento de textos. (Ejercicios 11 a 15)

---

## Conceptos de Programación Aplicados (Con Ejemplos)

A lo largo de los ejercicios se dominan múltiples estructuras:

### 1. Condicionales (`if`, `elif`, `else`)
Usados para tomar decisiones lógicas en base al valor de variables.

**Ejemplo del Ejercicio 2 (Mayoría de edad):**
```python
edad = int(input("¿Cuál es tu edad? "))
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Aún eres menor de edad.")
```

### 2. Bucles (`while` y `for`)
El bucle `while` se repite mientras una condición sea verdadera, ideal para cuando no sabemos cuántas veces debe ejecutarse el código.

**Ejemplo `while` (Ejercicio 8 - Adivina el número):**
```python
intento = 0
numero_secreto = 50
while intento != numero_secreto:
    intento = int(input("Tu intento: "))
    if intento < numero_secreto:
        print("Es mayor.")
# El bucle acabará cuando intento sea igual a numero_secreto
```

El bucle `for` se emplea cuando es necesario iterar un número conocido de veces o a lo largo de una colección (como listas o strings).

**Ejemplo `for` (Ejercicio 10 - Fibonacci):**
```python
a, b = 0, 1
for _ in range(5):
    print(a)
    a, b = b, a + b
```

### 3. Listas y Diccionarios
Las **listas** almacenan múltiples elementos en orden. Los **diccionarios** guardan datos en formato `clave: valor`.

**Ejemplo Lista (Ejercicio 11 - Ordenamiento):**
```python
lista = [34, 1, 56, 12]
# Intercambiar elementos de una lista
lista[0], lista[1] = lista[1], lista[0]
print(lista) # Muestra: [1, 34, 56, 12]
```

**Ejemplo Diccionario (Ejercicio 14 - Frecuencia de palabras):**
```python
frecuencias = {}
palabra = "python"
# Si la palabra no existe, la crea con valor 0 y le suma 1
frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
```

### 4. Funciones (`def`)
Las funciones encapsulan bloques de código que hacen tareas específicas, para poder ser reutilizados.

**Ejemplo de Función (Estructura general del script `resultados_totales.py`):**
```python
def ejercicio_3():
    numero = 4
    if numero % 2 == 0:
        print("Par")
        
# La llamamos así:
ejercicio_3()
```
