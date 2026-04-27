# SOLUCIÓN AL EJERCICIO 3
# Dada una lista vacía, utiliza un bucle for para agregar los números pares del 2 al 10 e imprime la lista.

pares = []
for i in range(2, 11, 2):
    pares.append(i)
print('Números pares:', pares)

# Explicación: Se usa range con saltos de 2 y se agregan los números usando append().
