#Desafio 1
# num = int(input("Ingresá un número: "))

# if num % 2 == 0:
#     print("Es par")
# else:
#     print("Es impar")


#Desafio 2
# num = int(input("Ingresá un número: "))
# if num % 2 == 0:
#     print("Es múltiplo de 2")
# elif num % 3 == 0:
#     print("Es múltiplo de 3")
# elif num % 5 == 0:
#     print("Es múltiplo de 5")
# else:
#     print("No es múltiplo de 2, 3 ó 5")


#Desafio 3
# letra = input("Ingresá una letra: ")
# if letra >= 'a' and letra <= 'z':
#     print("Es minúscula")
# elif letra >= "A" and letra <= "Z":
#     print("Es mayúscula")
# else:
#     print("No es una letra")

#Desafio 4
# caracter = input("Ingresa un caracter: ")
# if caracter == '\"':
#     print("Es una comilla")
# else:
#     print("NO es una comilla")

#Desafio 5
# cadena1 = input("Ingresá una palabra: ")
# cadena2 = input("Ingresá otra palabra: ")
# if len(cadena1) > len(cadena2):
#     print(cadena1)
# else:
#     print(cadena2)

#Desafio 6
cadena = input("Ingrese una palabra: ")
cantidad = 0
for car in cadena:
    if car == "a":
        cantidad = cantidad + 1
print(f"Cantidad de letras \"a\": {cantidad}")