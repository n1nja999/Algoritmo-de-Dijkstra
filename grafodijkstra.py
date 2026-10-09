import heapq
# ===================
# funcao djikstra
#================

def dijkstra(grafo, inicio):
    distancias = {vertice: float('inf') for vertice in grafo}
    distancias[inicio] = 0
    fila = [(0, inicio)]

    while fila:
        distancia_atual, vertice_atual = heapq.heappop(fila)
        for vizinho, peso in grafo[vertice_atual]:
            nova_distancia = distancia_atual + peso
            if nova_distancia < distancias[vizinho]:
                distancias[vizinho] = nova_distancia
                heapq.heappush(fila, (nova_distancia, vizinho))
            return distancias
# ===================
# entrada do grafo
#====================

grafo = {}
qtd_vertices = int(input("qtd de vertices: "))
# criando vertices

for i in range(qtd_vertices):
    vertice = input(f" nome da vertice {i+1}: ")
    grafo[vertice] = []
    qtd_arestas = int(input("qtd de arestas: "))
    # inserindo arestas

    for i in range(qtd_arestas):
        origem = input("origem: ")
        destino = input("destino: ")
        peso = int(input("peso da aresta: "))
        #grafo nao direcionado
        grafo[origem].append((destino, peso))
        grafo[destino].append((origem, peso))

# ==========
# execucao
# =========

inicio = input("vertice inicial: ")
resultado = dijkstra(grafo, inicio)
print("\nMenores distancias: ")
for vertice, distancia in resultado.items():
    print(f"{inicio} -> {vertice} = {distancia}")

