# -*- coding: utf-8 -*-
"""ComponentesConex

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XSPc5mNVp8wxXAsNv3ZDc_1IZuJnRLEB
"""

vertices = ["a", "b", "c", "d", "e", "f", "g", "h",
            "i", "j", "k", "l", "m", "n", "o", "p",
            "q", "r", "s", "t", "u", "v", "w", "x",
            "y", "z"]
casos = []
numeroDeTestes = int(input())

for teste in range(0, numeroDeTestes):
    grafo = []
    entrada = input()
    entradaSeparada = entrada.split()
    numV = int(entradaSeparada[0])
    numE = int(entradaSeparada[1])
    
    #Adicionando todos os vertices ao meu grafo.
    for i in range(0, numV):
        grafo.append(list())
        grafo[i].append(vertices[i])

    for c in range(0, numE):
        entradaE = input()
        entradaESeparada = entradaE.split()
        entradaE1 = entradaESeparada[0]
        entradaE2 = entradaESeparada[1]

        if(entradaE1 > entradaE2):
            #Faço essa transferencia de dados para tratar erros.
            #Sempre a entrada2 será adicionada na entrada1.
            #Como a entrada1 sempre será menor por meio dessa manipulação abaixo
            #Eu tenho uma manipulação padronizada dos subgrafos.
            aux = entradaE1
            entradaE1 = entradaE2
            entradaE2 = aux
        
        for index, subgrafo in enumerate(grafo):   
            
            if((entradaE1 in subgrafo) and (entradaE2 in subgrafo)):
                break

            #Manipulando as arestas dadas e organizando em subgrafos.
            if(entradaE1 in subgrafo):
                for i, subgrafo2 in enumerate(grafo):
                    if(entradaE2 in subgrafo2):
                        for x, item in enumerate(subgrafo2):
                            #Pego todos os itens que estão no subgrafo da entrada2
                            #Adiciono no subgrafo da entrada1.
                            subgrafo.append(item)
                        grafo.remove(subgrafo2)
                        break
                break
                
    #Adicionando aos casos.
    casos.append(grafo)   

#Organizando os Grafos em ordem alfabética:
for indexGrafo in range(0, len(casos)):
    for indexSubgrafo in range(0, len(casos[indexGrafo])):
        casos[indexGrafo][indexSubgrafo].sort()
    casos[indexGrafo].sort()


#Output
for c in range(0, len(casos)):
    print("Case #" + str(c+1) + ":")    
    for indexGrafo in range(0, len(casos[c])):
        for indexSubgrafo in range(0, len(casos[c][indexGrafo])):
            print(str(casos[c][indexGrafo][indexSubgrafo]) + ',', end='' )
        print()
    print(str(len(casos[c])) + " connected components")
    print()