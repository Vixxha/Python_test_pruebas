# SOLUCIÓN AL EJERCICIO 3
# Obtén e imprime todas las claves y valores del diccionario `auto = {'marca': 'Toyota', 'modelo': 'Corolla'}` utilizando un bucle.

auto = {'marca': 'Toyota', 'modelo': 'Corolla'}
for clave, valor in auto.items():
    print(f'{clave}: {valor}')

# Explicación: El método items() devuelve pares clave-valor que se pueden iterar en el bucle.
