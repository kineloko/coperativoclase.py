import random
from grupos import subLista

def main():
    lista1 = []

    pregunta = int(input("Ingrese numero de integrantes en la lista: "))

    i = 0

    while i < pregunta:
        lista2 = input(f"ingrese nombre {i+1} de {pregunta}: ")
        lista1.append(lista2)
        i += 1

    random.shuffle(lista1)
    subLista(lista1)