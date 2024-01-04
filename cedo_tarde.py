import networkx as nx

def calcular_tempo_mais_cedo(grafo):
    tempo_cedo = {} #dicionario vazio
    for node in nx.topological_sort(grafo):#loop em ordem topologica
        max_tempo_cedo = 0
        for predecessor in grafo.predecessors(node):
            max_tempo_cedo = max(max_tempo_cedo, tempo_cedo[predecessor] + grafo[predecessor][node]['tempo'])#compara o valor atual com a soma do tempo mais cedo do predecessor e a duração da aresta entre o predecessor e o vertice atual.
        tempo_cedo[node] = max_tempo_cedo

    return tempo_cedo

def calcular_tempo_mais_tarde(grafo, tempo_cedo):
    tempo_tarde = {}
    for node in grafo.nodes():
        tempo_tarde[node] = float('inf')#definindo tempo mais tarde como infinito

    tempo_tarde[list(grafo.nodes())[len(grafo.nodes()) - 1]] = tempo_cedo[list(grafo.nodes())[len(grafo.nodes()) - 1]]#igualando tempo do ultimo vertice 

    for node in reversed(list(nx.topological_sort(grafo))):#loop em ordem invertida
        for successor in grafo.successors(node):
            tempo_tarde[node] = min(tempo_tarde[node], tempo_tarde[successor] - grafo[node][successor]['tempo'])#tempo mais tarde para o vertice atual com base no tempo mais tarde do sucessor e na duração da aresta entre eles

    return tempo_tarde

def encontrar_caminho_critico(grafo, tempo_cedo, tempo_tarde):
    caminho_critico = []
    for node in grafo.nodes():
        if tempo_cedo[node] == tempo_tarde[node]:
            caminho_critico.append(node)
    return caminho_critico


if __name__ == "__main__":
    arquivo_entrada = "tempo.txt"  

    grafo = nx.read_edgelist(arquivo_entrada, create_using=nx.DiGraph(), data=[('tempo', int)])

    tempo_cedo = calcular_tempo_mais_cedo(grafo)
    tempo_tarde = calcular_tempo_mais_tarde(grafo, tempo_cedo)
    caminho_critico = encontrar_caminho_critico(grafo, tempo_cedo, tempo_tarde)

    for node in grafo.nodes():
        print(f"Vértice {node}: Tempo mais cedo = {tempo_cedo[node]}, Tempo mais tarde = {tempo_tarde[node]}")

    print("Caminho Crítico:")
    print(caminho_critico)