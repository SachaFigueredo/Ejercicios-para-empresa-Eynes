import pytest
from simple import lista_ordenada, lista_generada

def test_lista_ordenada(lista_generada):
    assert lista_ordenada(lista_generada) == [{'id': 10, 'edad': 100}, {'id': 9, 'edad': 99}, {'id': 8, 'edad': 98}, {'id': 7, 'edad': 97}, {'id': 6, 'edad': 96}, {'id': 5, 'edad': 95}, {'id': 4, 'edad': 94}, {'id': 3, 'edad': 93}, {'id': 2, 'edad': 92}, {'id': 1, 'edad': 91}]