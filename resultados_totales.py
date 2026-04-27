"""
SOLUCIONES TOTALES (EJERCICIOS 1 AL 15)

Aquí tienes el código de respuesta para cada uno de los ejercicios.
Están separados por funciones para que puedas probar el que necesites llamando a la función.
Por ejemplo, al final del archivo podrías escribir: ejercicio_10() y luego ejecutar el script.
"""
import random
import string

# ==========================================
# NIVEL BÁSICO
# ==========================================

# Ejercicio 1: Calculadora (solo dividir)
def ejercicio_1():
    try:
        n1 = float(input("Escriba un numero: "))
        n2 = float(input("Escriba otro numero: "))
        if n2 == 0:
            print("Error: NO se puede dividir en 0")
        else:
            print(f"El resultado es {n1 / n2}")
    except ValueError:
        print("Entrada no válida")

# Ejercicio 2: Mayor de edad
def ejercicio_2():
    edad = int(input("¿Cuál es tu edad? "))
    if edad >= 18:
        print("Eres mayor de edad.")
    else:
        print("Aún eres menor de edad.")

# Ejercicio 3: Par o impar
def ejercicio_3():
    numero = int(input("Introduce un número entero: "))
    if numero % 2 == 0:
        print(f"El {numero} es PAR.")
    else:
        print(f"El {numero} es IMPAR.")

# Ejercicio 4: Interés compuesto
def ejercicio_4():
    capital = float(input("Cantidad a invertir: "))
    interes = float(input("Interés anual (%): "))
    anios = int(input("Número de años: "))
    
    capital_final = capital * ((1 + (interes / 100)) ** anios)
    print(f"El capital obtenido tras {anios} años será de: {round(capital_final, 2)}")

# Ejercicio 5: Invertir palabra
def ejercicio_5():
    palabra = input("Escribe una palabra: ")
    print(f"Palabra invertida: {palabra[::-1]}")

# Ejercicio 16: Área del triángulo
def ejercicio_16():
    try:
        base = float(input("Escribe la base del triángulo: "))
        altura = float(input("Escribe la altura del triángulo: "))
        area = (base * altura) / 2
        print(f"El área del triángulo es: {area}")
    except ValueError:
        print("Entrada no válida")

# Ejercicio 17: Temperatura
def ejercicio_17():
    try:
        celsius = float(input("Escribe la temperatura en grados Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C equivalen a {fahrenheit}°F")
    except ValueError:
        print("Entrada no válida")

# Ejercicio 18: Descuento
def ejercicio_18():
    try:
        precio = float(input("Escribe el precio del producto: "))
        precio_final = precio - (precio * 0.15)
        print(f"El precio con 15% de descuento es: {precio_final}")
    except ValueError:
        print("Entrada no válida")

# ==========================================
# NIVEL INTERMEDIO
# ==========================================

# Ejercicio 6: Contar vocales
def ejercicio_6():
    frase = input("Escribe una frase: ").lower()
    nvocales = sum(1 for letra in frase if letra in "aeiouáéíóú")
    print(f"La frase tiene {nvocales} vocales.")

# Ejercicio 7: Palíndromo
def ejercicio_7():
    palabra = input("Introduce una palabra o frase corta: ").lower()
    palabra_limpia = palabra.replace(" ", "")
    if palabra_limpia == palabra_limpia[::-1]:
        print("¡Es un palíndromo!")
    else:
        print("No es un palíndromo.")

# Ejercicio 8: Adivina el número
def ejercicio_8():
    numero_secreto = random.randint(1, 100)
    intento = 0
    print("Adivina el número del 1 al 100.")
    while intento != numero_secreto:
        try:
            intento = int(input("Tu intento: "))
            if intento < numero_secreto:
                print("El número buscado es mayor.")
            elif intento > numero_secreto:
                print("El número buscado es menor.")
        except ValueError:
            print("Por favor, introduce un número válido.")
    print("¡Correcto! Has adivinado el número.")

# Ejercicio 9: Generador de contraseñas
def ejercicio_9():
    longitud = 12
    caracteres = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(caracteres) for _ in range(longitud))
    print(f"Contraseña generada: {password}")

# Ejercicio 10: Sucesión de Fibonacci
def ejercicio_10():
    try:
        n = int(input("¿Cuántos términos de Fibonacci quieres ver?: "))
        a, b = 0, 1
        serie = []
        for _ in range(n):
            serie.append(str(a))
            a, b = b, a + b
        print("Sucesión: " + ", ".join(serie))
    except ValueError:
        print("Entrada no válida.")

# ==========================================
# NIVEL AVANZADO
# ==========================================

# Ejercicio 11: Ordenar lista (Bubble Sort)
def ejercicio_11(lista=[34, 1, 56, 12, 9, 88, 3]):
    print(f"Lista original: {lista}")
    n = len(lista)
    # Copiamos la lista para no alterar la original
    lista_ordenada = lista.copy()
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_ordenada[j] > lista_ordenada[j + 1]:
                lista_ordenada[j], lista_ordenada[j + 1] = lista_ordenada[j + 1], lista_ordenada[j]
                
    print(f"Lista ordenada: {lista_ordenada}")
    return lista_ordenada

# Ejercicio 12: Números romanos
def ejercicio_12():
    try:
        num = int(input("Introduce un número entero (1-3999): "))
        if num < 1 or num > 3999:
            print("El número debe estar entre 1 y 3999.")
            return
        
        valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        simbolos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        romano = ""
        i = 0
        original = num
        
        while num > 0:
            for _ in range(num // valores[i]):
                romano += simbolos[i]
                num -= valores[i]
            i += 1
            
        print(f"El número {original} en romanos es: {romano}")
    except ValueError:
        print("Entrada no válida.")

# Ejercicio 13: El Ahorcado (Consola)
def ejercicio_13():
    palabra = random.choice(["python", "programacion", "desarrollo", "computadora"])
    adivinadas = []
    intentos = 6
    print("¡Bienvenido al juego del Ahorcado!")
    
    while intentos > 0:
        estado = ""
        for letra in palabra:
            if letra in adivinadas:
                estado += letra + " "
            else:
                estado += "_ "
        print(f"\nPalabra: {estado}")
        
        if "_" not in estado:
            print("¡Ganaste! Adivinaste la palabra correctamente.")
            return
            
        print(f"Intentos restantes: {intentos}")
        letra_intento = input("Introduce una letra: ").lower()
        
        if len(letra_intento) != 1 or not letra_intento.isalpha():
            print("Por favor, introduce solo una letra válida.")
            continue
            
        if letra_intento in adivinadas:
            print("Ya has intentado esa letra.")
            continue
            
        if letra_intento in palabra:
            print("¡Correcto!")
            adivinadas.append(letra_intento)
        else:
            print("Incorrecto.")
            adivinadas.append(letra_intento) # Para que no la repita, pero resta intentos
            intentos -= 1
            
    print(f"\nPerdiste. Has agotado tus intentos. La palabra era '{palabra}'.")

# Ejercicio 14: Frecuencia de palabras
def ejercicio_14():
    texto = input("Escribe un texto o frase larga:\n")
    texto = texto.lower()
    for signo in ",.:;!?¡¿\"'()":
        texto = texto.replace(signo, "")
        
    palabras = texto.split()
    frecuencias = {}
    for p in palabras:
        frecuencias[p] = frecuencias.get(p, 0) + 1
        
    print("\nFrecuencia de palabras:")
    for pal, frec in sorted(frecuencias.items(), key=lambda item: item[1], reverse=True):
        print(f" - '{pal}': {frec} veces")

# Ejercicio 15: Tres en Raya
def ejercicio_15():
    tablero = [" "]*9
    turno = "X"
    
    def mostrar_tablero():
        print(f"\n {tablero[0]} | {tablero[1]} | {tablero[2]}")
        print("---+---+---")
        print(f" {tablero[3]} | {tablero[4]} | {tablero[5]}")
        print("---+---+---")
        print(f" {tablero[6]} | {tablero[7]} | {tablero[8]}\n")
        
    def verificar_victoria():
        wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        for w in wins:
            if tablero[w[0]] == tablero[w[1]] == tablero[w[2]] != " ":
                return tablero[w[0]]
        return None

    print("=== Tres en Raya ===")
    print("Posiciones tablero (0-8):")
    print(" 0 | 1 | 2 \n---+---+---\n 3 | 4 | 5 \n---+---+---\n 6 | 7 | 8 ")
    
    while True:
        mostrar_tablero()
        try:
            mov = int(input(f"Turno de {turno} (0-8): "))
            if mov < 0 or mov > 8:
                print("Movimiento no válido.")
                continue
                
            if tablero[mov] == " ":
                tablero[mov] = turno
                ganador = verificar_victoria()
                if ganador:
                    mostrar_tablero()
                    print(f"¡El jugador {ganador} ES EL GANADOR!")
                    break
                if " " not in tablero:
                    mostrar_tablero()
                    print("¡Es un EMPATE!")
                    break
                turno = "O" if turno == "X" else "X"
            else:
                print("Esa posición ya está ocupada.")
        except ValueError:
            print("Por favor, introduce un número del 0 al 8.")

# Llama a la función que quieras probar aquí abajo:
# Por ejemplo:
# ejercicio_10()
