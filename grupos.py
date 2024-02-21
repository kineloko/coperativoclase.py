def subLista(lista1):
    subListas = [lista1[i:i+5] for i in range(0,len(lista1),5)]
    for i, subLista in enumerate(subListas, start=1):
        impresion = print(f"sublista {i}: {subLista}")
    return impresion