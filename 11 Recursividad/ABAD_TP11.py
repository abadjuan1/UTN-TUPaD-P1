# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario

#def factorial(num):
#    return 1 if num == 0 else num * factorial(num-1)
#
#num = int(input("Ingrese un numero: "))
#for i in range (1, num +1):
#    print(f"El factorial de {i} es {factorial(i)}")

#---------------------------------------------------------------------------------------------------------------

# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique 

#def fibonacci (pos):
#    if pos == 0:
#        return 0
#    elif pos == 1:
#        return 1
#    else:
#        return fibonacci(pos-1) + fibonacci (pos-2)

#posicion = int(input("Ingresa el numero de posicion hasta el que quieres imprimir: "))
#for i in range (posicion+1):
#    print (fibonacci(i), end = " ")

#---------------------------------------------------------------------------------------------------------------

# 3)Crea una función recursiva que calcule la potencia de un número base elevado a un
#exponente, utilizando la fórmula 𝑛^𝑚 = 𝑛 ∗ 𝑛^(𝑚−1). Prueba esta función en un
# algoritmo general.

#def potencia(numero, exponente):
#    if exponente == 0:
#        return 1
#    else: 
#        return numero * potencia(numero, exponente-1)
# FUNCION INVOCADA DESDE MAIN.PY

#---------------------------------------------------------------------------------------------------------------

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base
# decimal y devuelva su representación en binario como una cadena de texto.

#def binario(num):
#    if num == 0:
#        return str(0)
#    elif num == 1:
#        return str(1)
#    else: 
#        return binario (num // 2) + str (n % 2)

#n = int(input("Ingrese el numero en base decimal que quiere convertir a binario: "))
#print(f"El numero {n} en binario es {binario(n)}")        

#---------------------------------------------------------------------------------------------------------------

# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
#cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.

#def es_palindromo(palabra):
#    if len(palabra) <= 1:
#        return True
#    elif palabra[0] != palabra[len(palabra)-1]:
#        return False
#    else:
#        return es_palindromo(palabra[1:-1]) #Se forma una nueva cadena desde la posicion 1 a la penultima, achicando la palabra

#palabra = input("Ingrese una cadena de texto sin espacios ni tildes: ")
#print("Es palindromo") if es_palindromo(palabra) else print("No es palindromo")

#---------------------------------------------------------------------------------------------------------------

# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.

#def suma_digitos(n):
#    if n < 10:
#        return n
#    else:
#        return n % 10 + suma_digitos(n//10) 
    
#num = int(input("Ingrese un numero para calcular la suma de sus digitos: "))
#print(f"La suma de los digitos de {num} es {suma_digitos(num)}")

#---------------------------------------------------------------------------------------------------------------

# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
# último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide.

#def contar_bloques(n):
#    if n == 1:
#        return 1
#    else: 
#        return contar_bloques(n-1) + n
    
#piso = int(input("Ingrese la cantidad de bloques del piso mas bajo: "))
#print(f"La piramide necesita {contar_bloques(piso)} bloques para ser constuida")   

#---------------------------------------------------------------------------------------------------------------

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número. 

#def contar_digito(numero, digito):
#    if numero == 0:
#        return 0
#    elif numero % 10 == digito: #comparo el ultimo digito de mi numero
#        return 1 + contar_digito(numero // 10, digito)
#    else:
#        return contar_digito(numero // 10, digito) #Si no es igual, sigo pero sin el ultimo numero(el resto)
    
#num = int(input("Ingrese un numero entero positivo: "))
#dig = int(input("Ingrese un numero entre 0 y 9: "))
#print(f"El numero {dig} aparece en {num}: {contar_digito(num, dig)} veces")