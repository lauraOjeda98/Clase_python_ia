# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 19:24:18 2021

@author: laura
"""

# Tipos de Colecciones

# Listas o vectores
# Tipos de dato mutable y ordenado
a = []
a = [2, 3, 4]
b = [2, True, 'Hola', 3.4]
c = [2, [3, 4], ['Hola', 'Mundo'], [2.3, [2.4, 2.5], 2.6]]

for i in a:
    print(i)

for i in b:
    print(i)

for i in c:
    print(i)

a[0] = 7
print(b[2])
print(c[2][0])
print(c[2][1])
print(c[3][1][1])

a.append(5)  # Agrega el elemento al final de la vista
a.append(3)
a.remove(3)  # Elimina el elemento que coincida
a.pop()  # Elimina el último elemento del vector
a.pop(2)  # Elimina por posición
# a.clear()  # Elimina todos los elementos del vector

# a = [2, True, 'Hola', 3.4]
# del a

4 in a  # Busca el elemento 4 dentro de a
len(a)  # Cantidad de elementos del vector
a = b  # asignación de b en el mismo espacio de memoria de a
id(a)  # Convierte a décimal la dirección en memoria
a = b.copy()  # Copia los elementos de b en a
a = b[:]  # Forma más sencila
b = a[0:3]
b = a[:6]
b = a[2:]
c = [2, [3, 4], ['Hola', 'Mundo'], [2.3, [2, 5, 7], 2.6]]
d = c[3][1[:2]]

# Tuplas
# Tipos de dato INMUTABLE y ordenado

a = ()
a = (1, 2, 3, 4)
print(a[1])
a = (2, 3, 4)
b = (2, True, 'Hola', 3.4)
c = (2, [3, 4], ['Hola', 'Mundo'], [2.3, [2.4, 2.5], 2.6])

4 in a

# Set
# Mutable pero NO ordenado

a = set()
a = {1, 2, 3, 4}
print(a[1])
a = {2, 3, 4}
b = {2, True, 'Hola', 3.4}
# c = {2, [3, 4], ['Hola', 'Mundo'], [2.3, [2.4, 2.5], 2.6]}
# No permite array en su interior

4 in a

# Diccionario
# Muteable y No ordenado

a = {}
a = {'nombre': 'Roberto', 'apellido': 'Morales'}
a = {1: 'Roberto', 2: 'Morales'}

a['nombre']

for i in a:
    print(i)

for i in a.values():
    print(i)

for i in a.keys():
    print(i)

for i in a.items():
    print(i)

for llave, valor in a.items():
    print(f"Llave: {llave}, Valor: {valor}")

# Funciones


def nombre_funcion():
    pass


def saludar():
    print('Hola mundo')


def saludar(nombre):  # Python no permite sobrecarga de métodos
    print(f"Hola {nombre}")

# Parámetros opcionales


def saludar(nombre='Mundo'):
    print(f"Hola {nombre}")


def saludar(nombre="", apellido=""):
    print(f"Hola {nombre} {apellido}")


# No se puede tener un parámetro obligatorio después de un parámetro opcional
# def saludar(nombre, apellido="", segundo_apellido):
#    print(f"Hola {nombre} {apellido}")

# Parámetros ilimitados
def saludar(*nombres):
    for nombre in nombres:
        print(f"Hola {nombre}")


def saludar(*nombres, apellido=""):
    for nombre in nombres:
        print(f"Hola {nombre}")
    print(f"Apellido {apellido}")


def saludar(**nombres):
    print(nombres)


def resta(a, b):
    print(a-b)


def operaciones(a, b):
    suma = a + b
    resta = a - b
    mult = a * b
    div = a / b
    return suma, resta, mult, div


resultados = operaciones(a, b)

suma, res, mult, div = operaciones(4, 5)
suma, _, _, div = operaciones(4, 5)
suma, div = operaciones(4, 5)

# While(condición):