#   1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
#   (incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 

#for x in range(0,101):
#    print(x)

#   2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
#   dígitos que contiene. 

#numero = int(input("Ingrese un numero entero"))
#numero_actual = numero
#contador = 0
#while numero_actual != 0:
#    numero_actual = numero_actual // 10
#    contador = contador + 1
#print(f"El numero {numero} tiene {contador} digitos")    


#   3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
#   dados por el usuario, excluyendo esos dos valores. 

#a = int(input("Ingrese un numero entero"))
#b = int(input("Ingrese otro numero entero"))
#acumulador = 0
#for x in range (a+1, b):
#    acumulador += x
#print(f"El resultado de sumar los valores comprendidos entre {a} y {b} es {acumulador}")


#   4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
#   secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
#   un 0. 

#acu = 0
#num = int(input("Ingrese un numero para acumular, para cortar ingrese 0"))
#while num != 0:
#    acu += num 
#    num = int(input("Ingrese otro numero para acumular, para cortar ingrese 0"))
#print(f"El total acumulado es {acu}")

#   5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
#   programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 

#import random
#numero_a_adivinar = random.randint(0,9)
#print(f"El numero a adivinar es {numero_a_adivinar}")
#contador = 0
#intento = -1 
#while intento != numero_a_adivinar:
#    intento = int(input("Intente adivinar el numero"))
#    contador += 1
#print(f"Adivino el numero {numero_a_adivinar} en {contador} intentos")

#   6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
#   entre 0 y 100, en orden decreciente. 

#for x in range (100, -1, -2):
#    print(x)

#   7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
#   número entero positivo indicado por el usuario.

#numero = int(input("Ingrese un numero entero positivo"))
#acu = 0
#for x in range(0, numero+1):
#    acu += x
#print(f"El resultado de la suma de todos los numeros entre 0 y {numero} es {acu}")

#   8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
#   programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
#   negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
#   menor, pero debe estar preparado para procesar 100 números con un solo cambio). 

#cont_par = 0
#cont_impar = 0
#cont_pos = 0
#cont_neg = 0
#for x in range (100):
#    num = int(input("Ingrese un numero"))
#    if num > 0:
#       cont_pos += 1
#    elif num < 0:
#        cont_neg += 1
#    
#    if num % 2 == 0:
#        cont_par += 1
#    else: 
#        cont_impar += 1
#print(f"Hay {cont_pos} positivos, {cont_neg} negativos, {cont_par} pares y {cont_impar} impares")       

#   9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
#   media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
#   poder procesar 100 números cambiando solo un valor). 

#acu = 0
#for x in range (100):
#    num = int(input("Ingrese un numero"))
#    acu += num
#media = acu / 100
#print(f"La media de los valores ingresados es {media}")

#   10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
#   usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

#num = input("Ingrese un numero")
#cantidad = len(num)
#for x in range ((cantidad -1), -1, -1):
#    print(num[x], end = "")