import random

def generar_lista():
    lista = []
    for i in range(10):
        diccionario = {'id': i+1, 'edad': random.randint(1,100)}
        lista.append(diccionario)
    return lista

def ordenar_lista(lista):
    lista_ordenada = sorted(lista, key=lambda x: x['edad'], reverse=True)
    id_joven = lista_ordenada[-1]['id']
    id_viejo = lista_ordenada[0]['id']
    print(f"El id del mas joven es {id_joven} y el del mas viejo es {id_viejo}")
    return lista_ordenada

lista_generada = generar_lista()
lista_ordenada = ordenar_lista(lista_generada)

print(lista_ordenada)
