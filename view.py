
from LinkedList import *
from Node import *
def main():
    lista_ligada = LinkedList()
    while True:
        try:
            comandos = input().split(" ")
        except EOFError:
            return 
        if comandos[0] == "RPI":
            RPI(lista_ligada, comandos)
        if comandos[0] == "RPF":
            RPF(lista_ligada, comandos)
        if comandos[0] == "RPDE":
            RPDE(lista_ligada, comandos)
        if comandos[0] == "RPAE":
            RPAE(lista_ligada, comandos[2], comandos[1])
        if comandos[0] == "RPII":
            RPII(lista_ligada, comandos)
        if comandos[0] == "VNE":
            VNE(lista_ligada)
        if comandos[0] == "VP":
            VP(lista_ligada, comandos)
        if comandos[0] == "EPE":
            EPE(lista_ligada)
        if comandos[0] == "EUE":
            EUE(lista_ligada)
        if comandos[0] == "EP":
            EP(lista_ligada, comandos)

def RPI(lista_ligada, comandos):
    pais_novo = comandos[1]
    lista_ligada.insert_at_start(pais_novo)
    lista_ligada.traverse_list()

def RPF(lista_ligada, comandos):
    pais_novo = comandos[1]
    lista_ligada.insert_at_end(pais_novo)
    lista_ligada.traverse_list()

def RPDE(lista_ligada, comandos):
    pais_novo = comandos[2]
    pais_registado = comandos[1]
    lista_ligada.insert_after_item(pais_novo, pais_registado)
    lista_ligada.traverse_list()

def RPAE(lista_ligada, pais_registado, pais_novo):
    lista_ligada.insert_before_item(pais_registado, pais_novo)
    lista_ligada.traverse_list()

def RPII(lista_ligada, comandos):
    pais_novo = comandos[1]
    posiçao = int(comandos[2])
    lista_ligada.insert_at_index(posiçao, pais_novo)
    lista_ligada.traverse_list()

def VNE(lista_ligada):
    numero_elementos = lista_ligada.get_count()
    print(f"O número de elementos são {numero_elementos}.")

def VP(lista_ligada, comandos):
    nome_pais = comandos[1]
    if lista_ligada.search_item(nome_pais) == False:
        print(f"O país {nome_pais} não se encontra na lista")
    else:
        print(f"O país {nome_pais} encontra-se na lista.")

def EUE(lista_ligada):
    numero_eliminado = lista_ligada.get_last_node()
    lista_ligada.delete_at_end()
    print(f"O país {numero_eliminado} foi eliminado da lista.")

def EPE(lista_ligada):
    lista_ligada.reverse_linkedlist()
    numero_eliminado = lista_ligada.get_last_node()
    lista_ligada.delete_at_end()
    print(f"O país {numero_eliminado} foi eliminado da lista.")

def EP(lista_ligada, comandos):
    numero_eliminado = comandos[1]
    if lista_ligada.search_item(numero_eliminado) == True: 
        lista_ligada.delete_element_by_value(numero_eliminado)
        print(f"O país {numero_eliminado} foi eliminado da lista.")
    else:
        print(f"O país {numero_eliminado} não se encontra na lista.")
