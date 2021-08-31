# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 19:29:51 2021

@author: Usuario
"""

print('hello world')

# Variables
a = 3
print(type(a))

# Suma
a = 2
b = 5
c = a + b
print(c)

# Resta
a = 2
b = 5
c = a - b
print(c)

# Potencia
a = 2
b = 5
c = a**b
print(c)


# Tipos de datos
# String str
a = "hola mundo"
a = 'hola mundo'
b = " I can't do it"
c = 'Alias "Roberto"'

# Entero int
a = 5

# Decimal float
a = 5.6

# Booleano bool
x = True
y = False

# Conversiones
a = '3'
y = int(a)
print(y)
print(type(y))

a = 3
y = str(a)
print(y)
print(type(y))

# Concatenaciones
a = "hola"
b = "mundo"
c = a + " " + b

a = "hola"
b = a*5

# Captura por pantalla
nombre = input('Digite su nomnbre: ')
print('Hola', nombre)

print('Digite su nombre: ')
nombre = input()
print('Hola', nombre)

# HUA que sume dos numeros e imprima su resultado
num = input('Digite el primer número a sumar: ')
num2 = input('Digite el segundo número a sumar: ')
resul = int(num) + int(num2)
print("El resultado de la suma es: ", resul)

num = float(input('Digite el primer número a sumar: '))
num2 = float(input('Digite el segundo número a sumar: '))
resul = num + num2
# print("El resultado de la suma es: ", resul)
print(f'La suma de lso números {num} + {num2} es {resul}')

# Lea un número y lo eleve al cuadrado
numero = float(input('Digite el número a elevar al cuadrado: '))
resultado = numero**2
print(f'El número {numero} elevado al cuadrado es igual a: {resultado}')

# Tomar el valor de un producto, le aplique el 20% de un descuento, imprima el
# valor del producto inicial, el valor con desceunto y el valor ahorrado
valor_producto = float(input('Digite el valor del producto: '))
descuento = valor_producto*0.20
valor_total = valor_producto - descuento
print(f'El valor inicial del producto es: ${valor_producto:,}')
print(f'El valor del descuento es: ${descuento:,}')
print(f'El valor final del producto es: ${valor_total:,}')

vproduct = float(input('Digite el valor del producto: $'))
descuent = vproduct * 0.20
vfinal = vproduct - descuent
print(f'El valor inicial del producto es: ${vproduct:,}')
print(f'El valor del descuento es: ${descuent:,}')
print(f'El valor final del producto es: ${vfinal:,}')
