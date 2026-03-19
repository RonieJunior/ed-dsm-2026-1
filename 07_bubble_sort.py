def bubble_sort(lista):
    """
    ALGORITMO DE ORDENAÇÃO BUBBLE SORT
    Percorre a lista a ser ordenada em sucessivas passadas,
    trocando entre si dois elementos adjacentes sempre que
    o SEGUNDO for MENOR do que o PRIMEIRO. Efetua tantas 
    passadas quanto necessárias, até que, na última passada,
    nenhuma troca tenha sido feita.
    """

    # Loop eterno: não sabemos com antecedência quantas
    # passadas serão necessárias para concluir a ordenação 
    while True:
         # Variável que controla se houve ou não troca durante
         # a passada
         trocou = False

         # Percorre a lista, do primeiro ao PENÚLTIMO elemento,
         # com acesso a cada posição
         for pos in range(len(lista) - 1):
            # Se o valor que está à frente na lista (pos + 1)
            # for MENOR do que o seu antecessor (pos), efetuamos
            # uma troca entre eles
            if lista[pos + 1] < lista[pos]:
                # Faz a troca (swap) direita
                lista[pos + 1], lista[pos] = lista[pos], lista[pos + 1]
                # Assinala que houve troca na passada
                trocou = True

    # <~ CUIDADO COM A IDENTAÇÃO AQUI!
    # Se não houve troca na passada (trocou ainda tem o valor False),
    # a lista está ordenada e interrompemos o loop while
    if not trocou: break

#####################################################################################

# Caso médio
# nums = [7, 0, 8, 1,=]

#####################################################################################

# TESTE COM 1M NOMES

from time import time

import sys
sys.dont_write_bytecode = True          # Destiva a criação do cache

from data.nomes_desord import nomes_desord

hora_ini = time()
bubble_sort (nomes)
hora_fim = time()

print(nomes)

print(f"Comparações: {comps}; trocas: {trocas}; passadas: {passd}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms.\n")