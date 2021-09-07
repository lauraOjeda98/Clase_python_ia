# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 19:02:07 2021

@author: Usuario
"""

# Condicionales
# Tabla de verdad

# Tabla del and
# v and v = v
# v and f = f
# f and v = f
# f and f = f

print(True and True)
print(True and False)
print(False and True)
print(False and False)

# Table del or
# v or v = v
# v or f = v
# f or v = v
# f or f = f

print(True or True)
print(True or False)
print(False or True)
print(False or False)

# Negación

print(not True)
print(not False)

# Más de dos condiciones al mismo tiempo

print(True and False and True or False or True or True)
print(True and (False and True) or False or (True or True))

# Jerarquía de operaciones
# 1. Parentesis y llaves
# 2. Potencias y Raíces
# 3. Multiplicación y División
# 4. Sumas y Restas

# Jerarquía de operaciones booleanas
# 1. Paréntesis y llaves
# 2. Tabla de verdad

# Estructura if
x = 1
if(x > 0):
    print("1")
else:
    print("2")
    print("3")

# Dada la edad de una persona indique si es mayor o menor de edad

edad = int(input("Ingrese su edad: "))
if (edad >= 18):
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")

# Indique si un estudiante aprobó o reprobó una asignatura teniendo
# en cuenta que aprueba con mínimo una cal de 3.0 hasta 5.0

nota = float(input("Ingrese su nota: "))
if (nota >= 3.0 and nota <= 5):
    print("Usted aprobó la asignatura")
elif(nota < 3.0 and nota > 0):
    print("Usted reprobó esta asignatura")
else:
    print("La nota ingresada no es válida")

# Dado un número n diga si es negativo, positivo o cero

num = float(input("Ingrese el número: "))
if (num > 0):
    print(f"El número {num} es positivo")
elif (num == 0):
    print("El número es cero")
else:
    print(f"El número {num} es negativo")

# Ciclos

# Ciclo for

for valor in (range(11)):
    print(valor)

for valor in (range(1, 11)):
    print(valor)

for valor in (range(2, 11, 2)):
    print(valor)

# Lea n notas de un estudiante y calcule el promedio final

n = int(input("Ingrese cantidad de notas a calcular: "))
notas = []
promedio = 0

for i in range(n):
    notas.append(float(input(f"Ingrese la {i+1} nota: ")))
    promedio = notas[i] + promedio

promedio = promedio/n
print(f"El promedio de las notas es de: {promedio}")

num = int(input("Digite número de notas cursadas: "))
if(num >= 0):
    acumulador = 0
    for x in range(num):
        nota = float(input(f"Digite la nota {x+1}: "))
        acumulador = acumulador + nota
        promedio = acumulador / num
        promedio = round(promedio, 2)
    print(f"El promedio final es: {promedio}")
else:
    print("El número no es válido")
