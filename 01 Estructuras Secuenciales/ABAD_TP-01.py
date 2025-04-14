# TRABAJO PRACTICO SECUENCIALES - JOSE JUAN DE LA CRUZ ABAD CORREA

# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("Hola Mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#realizar la impresión por pantalla.

nombre = input("Ingrese su nombre")
print(f"Hola {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.

nombre = input("Ingrese su nombre")
apellido = input("Ingrese su apellido")
edad = int(input("Ingrese su edad"))
domicilio = input("Ingrese su lugar de residencia")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {domicilio}")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.

radio = float(input("Ingrese el radio del circulo"))
area =  3.1416 * radio**2
perimetro = 2 * 3.1416 * radio
print(f"El area del circulo es {area} y el perimetro es {perimetro}")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.

segundos = int(input("Ingrese la cantidad de segundos"))
horas = segundos / 3600
print(f"{segundos} segundos equivale a {horas} horas")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.

numero = int(input("Ingrese un numero"))
print(f"{numero} * 1 = {numero * 1}")
print(f"{numero} * 2 = {numero * 2}")
print(f"{numero} * 3 = {numero * 3}")
print(f"{numero} * 4 = {numero * 4}")
print(f"{numero} * 5 = {numero * 5}")
print(f"{numero} * 6 = {numero * 6}")
print(f"{numero} * 7 = {numero * 7}")
print(f"{numero} * 8 = {numero * 8}")
print(f"{numero} * 9 = {numero * 9}")
print(f"{numero} * 10 = {numero * 10}")

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

a = int(input("Ingrese un numero distinto de 0"))
b = int(input("Ingrese otro numero distinto de 0"))
print(f"{a} + {b} = {a + b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} - {b} = {a - b}")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
#modo: IMC = peso en kg / (altura en m)**2

altura = float(input("Ingrese su altura"))
peso = float(input("Ingrese su peso"))
imc = peso / (altura)**2
print(f"Su indice de masa corporal es {imc}")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
# 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖 = 9/5 * 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32

celsius = float(input("Ingrese la temperatura en grados celsius"))
fahrenheit = 9/5 * celsius + 32
print(f"{celsius} grados celsius son {fahrenheit} grados fahrenheit")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números.

a = int(input("Ingrese el primer numero"))
b = int(input("Ingrese el segundo numero"))
c = int(input("Ingrese el tercer numero"))
promedio = (a + b+ c) / 3 
print(f"El promedio de los tres numeros es {promedio}")