
def es_par(numero):    
    if numero % 2 == 0:
        print("true")
        return True          
    else:
        print("False")
        return False  


def factorial(n):   
    if n == 0:
        return 1
    return n * factorial(n - 1)
    

def promedio_de_listas(lista_numeros):
    if lista_numeros:
        lista = sum(lista_numeros)/len(lista_numeros)
    else:
        print("Esto no es una lista")
    return lista
    

def area_circulo(entrada):
    if str(entrada).isdigit():
        radio = int(entrada)
        PI = 3.1416
        return PI * (radio ** 2)
    else: 
        print("Esto no es un numero positivo.")     
        
    

