from modulo import factorial
from modulo import es_par
from modulo import promedio_de_listas
from modulo import area_circulo

n = 6
print(f"Cual el factorial de {n}?")
print("El factorial es =", factorial(n))

print("-" * 40)

n = 6
print(f"Es par {n}?")
es_par(n)

print("-" * 40)

n = [1,2,3,4,5,6]
print(f"Cual es el promedio de {n}")
print(promedio_de_listas(n))

print("-" * 40)

n = 3
print(f"Cual es el radio de {n}")
print(area_circulo(n))

print("-" * 40)
