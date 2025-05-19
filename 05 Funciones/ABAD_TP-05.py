#1) Crear una función llamada imprimir_hola_mundo que imprima por
#pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#programa principal.

#def imprimir_hola_mundo():
#    print("Hola Mundo!")

#imprimir_hola_mundo()

#------------------------------------------------------------------------------------------------
#2) Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de
#volver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

#def saludar_usuario(nombre):
#    print(f"Hola {nombre}!")

#nombre = input("Ingresa tu nombre ")
#saludar_usuario(nombre)

#------------------------------------------------------------------------------------------------
#3) Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir
# los datos al usuario y llamar a esta función con los valores ingresados.

#def informacion_personal(nombre, apellido, edad, residencia):
#    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#nombre = input("Ingresa tu nombre ")
#apellido = input("Ingresa tu apellido ")
#edad = int(input("Ingresa tu edad "))
#residencia = input("Ingresa tu ligar de residencia ")
#informacion_personal(nombre, apellido, edad, residencia)

#------------------------------------------------------------------------------------------------
#4) Crear dos funciones: calcular_area_circulo(radio) que reciba el radio 
# como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) 
# que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio 
# al usuario y llamar ambas funciones para mostrar los resultados.

#import math
#def calcular_area_circulo(radio):
#    return math.pi * (radio**2)

#def calcular_perimetro_circulo(radio):
#    return 2 * math.pi * radio

#radio = float(input("Ingresa el radio del circulo: "))
#area = calcular_area_circulo(radio)
#perimetro = calcular_perimetro_circulo(radio)
#print(f"El area del circulo es {area} y el perimetro es {perimetro}")

#------------------------------------------------------------------------------------------------
#5) Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta 
# función.

#def segundos_a_horas(segundos):
#    return segundos/3600

#segundos = int(input("Ingrese la cantidad de segundos "))
#horas = segundos_a_horas(segundos)
#print(f"{segundos} segundos son {horas} horas")

#------------------------------------------------------------------------------------------------
#6) Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y 
# imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar 
# a la función.

#def tabla_multiplicar(numero):
#    for x in range(1, 11):
#        print(f"{numero} * {x} = {x * numero}")

#num = int(input("Ingresa un numero "))
#tabla_multiplicar(num)

#------------------------------------------------------------------------------------------------
#7) Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y
#  devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
# Mostrar los resultados de forma clara.

#def operaciones_basicas(a, b):
#    suma = a + b
#    resta = a - b
#    mult = a * b
#    if b == 0:
#        division = "No se puede dividir por 0"
#    else: 
#        division = a / b 
#    tupla = (suma, resta, mult, division)

#    return  tupla

#num1= int(input("Ingresa un numero "))
#num2 = int(input("Ingresa otro numero "))
#resultados = operaciones_basicas(num1, num2)
#print(f"La suma de {num1} y {num2} es {resultados[0]}")
#print(f"La resta de {num1} y {num2} es {resultados[1]}")
#print(f"La multiplicacion de {num1} y {num2} es {resultados[2]}")
#print(f"La division de {num1} y {num2} es {resultados[3]}")

#------------------------------------------------------------------------------------------------
#8) Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la 
# altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los 
# datos y llamar a la función para mostrar el resultado con dos decimales.

#def calcular_imc(peso, altura):
#    imc = peso / (altura**2)
#    return round(imc, 2)

#peso = float(input("Ingrese su peso en kg: "))
#altura = float(input("Ingrese su altura en metros: "))
#imc = calcular_imc(peso, altura)
#print(f"Su indice de masa corporal es de {imc}")

#------------------------------------------------------------------------------------------------
#9) Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario 
# la temperatura en Celsius y mostrar el resultado usando la función.

#def celsius_a_fahrenheit(celsius):
#    return(celsius * 9/5) + 32

#gradosC = float(input("Ingrese la temperatura en grados celsius: "))
#gradosF = celsius_a_fahrenheit(gradosC)
#print(f"{gradosC} grados celsius son {gradosF} grados fahrenheit")

#------------------------------------------------------------------------------------------------
#10) Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros 
# y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando 
# esta función

#def calcular_promedio(a, b, c):
#    return (a+b+c)/3

#num1 = int(input("Ingrese el primer numero: "))
#num2 = int(input("Ingrese el segundo numero: "))
#num3 = int(input("Ingrese el tercer numero: "))
#promedio = calcular_promedio(num1, num2, num3)
#print(f"El promedio de {num1}, {num2}, {num3} es {promedio}")