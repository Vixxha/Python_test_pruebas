# Solución a los Problemas de Librerías

Este documento contiene las soluciones a cada uno de los 9 problemas, separados por nivel de dificultad.

---

## Nivel Fácil

### Problema 1: Cálculo de Área (`math`)
```python
import math

radio = 5 
area = math.pi * (radio ** 2)
print(f"El área de un círculo de radio {radio} es: {area:.2f}")
```

### Problema 2: Dado Virtual (`random`)
```python
import random

resultado = random.randint(1, 6)
print(f"El número sacado de los dados es: {resultado}")
```

### Problema 3: Fecha Formateada (`datetime`)
```python
import datetime

hoy = datetime.datetime.now()
# strftime permite darle formato de string a la fecha
fecha_formateada = hoy.strftime("%d/%m/%Y")
print(f"La fecha de hoy es: {fecha_formateada}")
```

---

## Nivel Intermedio

### Problema 4: Días para Año Nuevo (`datetime`)
```python
import datetime

fecha_hoy = datetime.date.today()
proximo_ano = datetime.date(fecha_hoy.year + 1, 1, 1)
diferencia = proximo_ano - fecha_hoy
print(f"Faltan exactamente {diferencia.days} días para fin de año.")
```

### Problema 5: Frecuencia de palabras (`collections.Counter`)
```python
from collections import Counter

texto = "el perro corre rápido y el gato corre rápido"
# Se separan las palabras y se crea el contador directamente
frecuencia = Counter(texto.split())
print("Frecuencia de palabras:")
for palabra, cant in frecuencia.items():
    print(f" - {palabra}: {cant} veces")
```

### Problema 6: Sorteo (`random`)
```python
import random

participantes = ["Ana", "Juan", "Pedro", "Maria", "Luis", "Carmen"]

# 1. Barajar la lista
random.shuffle(participantes)
print(f"Lista desordenada: {participantes}")

# 2. Elegir un ganador
ganador = random.choice(participantes)
print(f"¡El ganador es {ganador}!")
```

---

## Nivel Difícil

### Problema 7: Contraseña Segura (`random` y `string`)
```python
import random
import string

def generar_password():
    # Obtener el mínimo obligatorio de 1 tipo cada uno
    mayuscula = random.choice(string.ascii_uppercase)
    minuscula = random.choice(string.ascii_lowercase)
    numero = random.choice(string.digits)
    especial = random.choice(string.punctuation)
    
    # Completar los 8 caracteres restantes aleatoriamente
    todos = string.ascii_letters + string.digits + string.punctuation
    extra = "".join(random.choice(todos) for _ in range(8))
    
    # Juntar y mezclar caracteres aleatoriamente
    lista_clave = list(mayuscula + minuscula + numero + especial + extra)
    random.shuffle(lista_clave)
    
    return "".join(lista_clave)

print(f"Contraseña de seguridad máxima: {generar_password()}")
```

### Problema 8: Aproximación de Pi (`math` y `random`)
```python
import random
import math

dentro = 0
total_puntos = 1_000_000

for _ in range(total_puntos):
    x = random.random()
    y = random.random()
    if (x**2 + y**2) <= 1:
        dentro += 1

pi_aprox = 4 * (dentro / total_puntos)
print(f"Estimación de Pi generada: {pi_aprox}")
```

### Problema 9: Agrupamiento por clave (`collections.defaultdict`)
```python
from collections import defaultdict

palabras = ["gato", "perro", "pájaro", "gallina", "lobo", "león", "puma"]

# Creamos un diccionario donde cada valor nuevo inicializa como una lista vacía []
diccionario_letras = defaultdict(list)

for palabra in palabras:
    primera_letra = palabra[0] # Obtiene la primera letra ("g", "p", etc)
    diccionario_letras[primera_letra].append(palabra)
    
# Iterando el diccionario para verlo mejor
for letra, lista in diccionario_letras.items():
    print(f"{letra}: {lista}")
```
