"Hacer un calculadora que divida solamente y que esta lance un error cuando sea = 0"

Num1 = float(input("Escriba un numero: "))
Num2 = float(input("Escriba otro numero "))

if Num1 or Num2 == 0:
    print ("Error NO se puede dividir en 0")
else:
    resultado = Num1 / Num2
    print ("El resultado es {resultado}")